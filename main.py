import requests
from collections import defaultdict

from basic_functions import *
from dijkstra_shortest_path_functions import *
from dfs_functions import *
from webscrape_functions import *

# start yelp search
search_results_dict = yelp_search_start()

# make a top 10 list with cleaner information
yelp_top_ten_list = yelp_result_list_maker(search_results_dict)

print('\n')

# view your top 10 list
yelp_print_entires(yelp_top_ten_list)

choice = input(
    'what function would you like to do (please look at user manual for inputs): ')

# options: 'shortest path between all', 'longest chain of satisfactory coffee shops', 'menu please', 'photos please',
# 'best path - game theory'


if choice == 'shortest path between all':
    # generates an adjacency list from dictionary of dictionaries
    yelp_sts = get_distances_of_all(yelp_top_ten_list)
    fixing_none_entries(yelp_sts)

    # name of all the top ten places
    for shop in yelp_top_ten_list:
        print('this is the name of a shop:', shop['name'])

    print('\n')

    # for referencing the numbers
    for shop in yelp_sts.items():
        print('here is one of the tables for the adjList:', shop, '\n')

    print('\n')

    # finding the shortest path, distance based on Yelp API
    # some interesting paths for coffee shops: Elixr Coffee -> Reanimator Coffee or Elixr Coffee -> Knockbox Cafe

    first_place = input(
        'please enter the name of the first location (cap sensitive): ')
    second_place = input(
        'please enter the name of the second location (cap sensitive): ')

    # returns the shortest path between two locations via parent pointers
    shortest_path, total_cost = dijkstra_shortest_path(
        yelp_sts, first_place, second_place)

    print('the shortest path between these two places is:',
          shortest_path, 'with a total distance of:', total_cost, 'miles')

elif choice == 'longest chain of satisfactory coffee shops':
    # adjacency list of happiness values
    yelp_sts = get_happiness_of_all(yelp_top_ten_list)

    for shop in yelp_top_ten_list:
        print('this is the name of a shop:', shop['name'])

    print('\n')

    starting_shop = input(
        'which shop would you like to start at? (case sensitive): ')

    starting_happiness = get_starting_happiness(
        starting_shop, yelp_top_ten_list)

    resulting_path = depth_first_search(
        yelp_sts, starting_shop, starting_happiness)

    # longest path in order of happiness
    resulting_path.reverse()

    # get the dfs path based on parent pointers
    previous_position = resulting_path[0][0]
    current_position = resulting_path[-1][0]
    the_increasing_happiness_path = list()

    while current_position is not None:
        the_increasing_happiness_path.append(
            (current_position, happiness_of_vertices[current_position]))
        previous_position = current_position
        current_position = parents_of_vertices[previous_position]

    the_increasing_happiness_path.reverse()

    print('the dfs path of longest chain of satisfactory coffee shops:',
          the_increasing_happiness_path, '\n')
    print('the longest path possible if starting at this path and only going to higher happiness coffee shops:',
          resulting_path)

elif choice == 'menu please':
    # first find the scrappable menus
    available_menus = scrappable_menus_list(yelp_top_ten_list)

    print('here are the available choices for menu scrapping:', available_menus)

    menu_selection = input(
        'please select a menu from the list (case sensitive): ')

    # scrapes the yelp menu website and gets prints the items and prices
    bring_up_menu(menu_selection, yelp_top_ten_list)

else:
    print('please try proper command; if you still get this error: i probably messed up')
