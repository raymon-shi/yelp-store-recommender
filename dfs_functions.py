from yelp_search import *
from basic_functions import *
from collections import defaultdict


def get_happiness_values_from_to(limited_list, compared_store):
    # if the two stores have the same id, then return the happiness
    for item in limited_list:
        if item['business_id'] == compared_store['business_id']:
            return item['happiness']


def get_happiness_of_all(yelp_top_list):
    print('creating connections, this may take a while....')
    yelp_store_to_store = dict()

    # compare each store with each other store
    for store in yelp_top_list:
        yelp_from_to_store = dict()
        for other_store in yelp_top_list:
            search_results = other_store_search(store, other_store)
            results_list = yelp_result_list_maker(search_results)
            happiness_to = get_happiness_values_from_to(
                results_list, other_store)

            # if the two stores don't have same id aka not the same store
            if store['business_id'] != other_store['business_id']:
                # make a key with store name and value of happiness to that store
                yelp_from_to_store[other_store['name']] = happiness_to

        # add that dictionary to the larger dictionary, representing larger dictionary vertex -> vertices of the smaller
        yelp_store_to_store[store['name']] = yelp_from_to_store
        print('function is running....')
    return yelp_store_to_store


def get_starting_happiness(store_name, yelp_list):
    # get the starting happiness for the starting store
    for store in yelp_list:
        if store['name'] == store_name:
            return store['happiness']


# keep track of which vertices are seen / which color stage they're at (0=white, 1=grey, 2=black)
color_of_vertices = defaultdict(lambda: 0)

# keep track of the happiness values for each vertext
happiness_of_vertices = defaultdict(lambda: 0)

# keep track of parents, used to build path
parents_of_vertices = defaultdict()

# longest dfs path
dfs_path = list()


def depth_first_search(graph, source, starting_happiness):
    parents_of_vertices[source] = None
    happiness_of_vertices[source] = starting_happiness
    depth_first_search_visit(graph, source, starting_happiness)

    return dfs_path


def depth_first_search_visit(graph, current_vertex, current_happiness):
    # currently exploring this vertex
    color_of_vertices[current_vertex] = 1
    # looking at all the neighbors of the current vertex
    for adj_vertex, happiness_value in graph[current_node].items():
        # if the color of neighbor is white and has a >= happiness value
        if color_of_vertices[adj_vertex] == 0 and happiness_value >= current_happiness:
            # update the parent pointer
            parents_of_vertices[adj_vertex] = current_vertex
            # update the happiness value
            happiness_of_vertices[adj_vertex] = happiness_value
            # start searching its neighbors
            depth_first_search_visit(graph, adj_vertex, happiness_value)

    # the current vertex is finished aka black
    color_of_vertices[current_vertex] = 2
    # add the finished vertex and its happiness value to the dfs path
    dfs_path.append((current_vertex, current_happiness))
