# from basic_functions import *
from collections import defaultdict
import heapq as min_heap
import random

from yelp_search import *
from basic_functions import *


def get_distance_from_to(limited_list, compared_store):
    # if the two stores have the same id, then return the distance
    for item in limited_list:
        if item['business_id'] == compared_store['business_id']:
            return item['distance']


def get_distances_of_all(yelp_top_list):
    print('creating connections, this may take awhile....')
    yelp_store_to_store = dict()

    # compare each store with each other store
    for store in yelp_top_list:
        yelp_from_to_store = dict()
        for other_store in yelp_top_list:
            search_results = other_store_search(store, other_store)
            results_list = yelp_result_list_maker(search_results)
            distance_to = get_distance_from_to(results_list, other_store)

            # if the two stores don't have same id aka not the same store
            if store['business_id'] != other_store['business_id']:
                # make a key with store name and value of distance to that store
                yelp_from_to_store[other_store['name']
                ] = distance_to

        # add that dictionary to the larger dictionary, representing larger dictionary vertex -> vertices of the smaller
        yelp_store_to_store[store['name']] = yelp_from_to_store
        print('function is running....')
    return yelp_store_to_store


def get_key(val, dict):
    for k, v in dict.items():
        if val == v:
            return k


# used to fix none entries from yelp api call return results
def fixing_none_entries(yelp_sts):
    iter = 1
    for item in yelp_sts.values():
        sum = 0
        iter = iter + 1
        if None in item.values():
            print('there is a none value at dictionary:', iter)
            for value in item.values():
                if value is not None:
                    sum = sum + value
                for value in item.values():
                    if value is None:
                        # once it finds the None value, generate the average of the current distances + some small random value
                        avg = sum / 9.0
                        random_avg = avg + (random.random() / 2.0)
                        print('this is the replacement value in the',
                              iter, 'dicitionary: ', random_avg)
                        key = get_key(value, item)
                        # then we go and find the original key that had a None value and replace the value
                        for k in item:
                            if key == k:
                                item[k] = random_avg


def dijkstra_shortest_path(graph, source, target):
    # check if source and target are valid
    if source not in graph.keys() or target not in graph.keys():
        return 'NOT VALID/DOES NOT EXIST', 'NOT VALID/DOES NOT EXIST'

    # used to recreate the path later
    parents_of_vertices = dict()

    # used as the queue
    queue = list()

    # initialize everything to infinity, just like regular dijkstra
    total_distance = defaultdict(lambda: float('inf'))

    # set the distance of the source to 0 and make it's parent nothing
    total_distance[source] = 0.00
    parents_of_vertices[source] = None

    # insert into the minheap
    min_heap.heappush(queue, source)

    # while not empty
    while len(queue) > 0:
        current_vertex = min_heap.heappop(queue)

        # check the neighbors
        for adj_vertex, edge_weight in graph[current_vertex].items():

            # if relaxation is possible, then do it
            if total_distance[adj_vertex] > total_distance[current_vertex] + edge_weight:
                relaxed_total_distance = total_distance[current_vertex] + edge_weight
                total_distance[adj_vertex] = relaxed_total_distance
                parents_of_vertices[adj_vertex] = current_vertex
                min_heap.heappush(queue, adj_vertex)

    previous_position = source
    current_position = target
    shortest_path = list()

    # produces the reverse path
    while current_position is not None:
        shortest_path.append(current_position)
        previous_position = current_position
        current_position = parents_of_vertices[previous_position]

    # reverse to get the proper path
    shortest_path.reverse()

    # get the total cost of the path
    total_cost = total_distance[shortest_path[-1]]

    return shortest_path, total_cost
