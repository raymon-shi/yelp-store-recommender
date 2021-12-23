from basic_functions import *
# from yelp_search import *
import requests


def get_key(val, dict):
    for k, v in dict.items():
        if val == v:
            return k


def player_A_search():
    term_A = input('player A establishment of interest to explore: ')
    limit_A_miles = input('player A enter the furthest distance you are willing to go in miles: ')
    limit_A_meters = miles_to_meters(limit_A_miles)
    location_A = input('player A Enter the your location (Address or Zip Code): ')
    price_A = input('player A Enter the maximum dollar sign amount you are willing to spend (max of 4):')
    price_A_fixed = dollar_sign_all(price_A)

    player_A_parameters = {
        'term': term_A,
        'limit': 10,
        'radius': limit_A_meters,
        'location': location_A,
        'price': price_A_fixed
    }

    resp = requests.get(url=yelp_businesses_search_url, params=player_A_parameters, headers=yelp_header)

    yelp_search_A_results = resp.json()
    a_list = yelp_result_list_maker(yelp_search_A_results)

    return a_list


def player_B_search():
    term_B = input('player B establishment of interest to explore: ')
    limit_B_miles = input('player B enter the furthest distance you are willing to go in miles: ')
    limit_B_meters = miles_to_meters(limit_B_miles)
    location_B = input('player B Enter the your location (Address or Zip Code): ')
    price_B = input('player B Enter the maximum dollar sign amount you are willing to spend (max of 4):')
    price_B_fixed = dollar_sign_all(price_B)

    player_B_parameters = {
        'term': term_B,
        'limit': 10,
        'radius': limit_B_meters,
        'location': location_B,
        'price': price_B_fixed
    }

    resp = requests.get(url=yelp_businesses_search_url, params=player_B_parameters, headers=yelp_header)

    yelp_search_B_results = resp.json()
    b_list = yelp_result_list_maker(yelp_search_B_results)

    return b_list


def best_strat(game_theory_dict):
    current_max = float('-inf')
    for value in game_theory_dict.values():
        if value > current_max:
            current_max = value

    best_strategy = get_key(current_max, game_theory_dict)

    print('the best strategy is:', best_strategy, 'with a utility of:', current_max)


def the_game_theory(player_a_list, player_b_list):
    total_happiness_A = 0
    total_happiness_B = 0

    for store_A, store_B in zip(player_a_list, player_b_list):
        total_happiness_A = total_happiness_A + store_A['happiness']
        total_happiness_B = total_happiness_B + store_B['happiness']

    base_game = {
        'Player A chooses A, Player B choose A': (total_happiness_A, total_happiness_A),
        'Player A chooses A, Player B choose B': (total_happiness_A, total_happiness_B),
        'Player A chooses B, Player B choose A': (total_happiness_B, total_happiness_A),
        'Player A chooses B, Player B choose B': (total_happiness_B, total_happiness_B)
    }

    print('here are the base values')
    for option in base_game.items():
        print(option)

    print('here are the rules that will change the base stats:')
    print('If Player A chooses A, then Player A gets +10% happiness')
    print('If Player B chooses A, then Player B gets -15% happiness')
    print('If Player A chooses B, then Player A gets -15% happiness')
    print('If Player B chooses B, then Player B gets +10% happiness')
    print('If Player A and Player B choose the same (A, A) or (B, B), then the apply deductions first, then apply a '
          '+20% happiness because they get to be together')

    updated_game = {
        'Player A chooses A, Player B choose A': (total_happiness_A * 1.1 * 1.2, total_happiness_A * .85 * 1.2),
        'Player A chooses A, Player B choose B': (total_happiness_A * 1.1, total_happiness_B * 1.1),
        'Player A chooses B, Player B choose A': (total_happiness_B * 0.85, total_happiness_A * 0.85),
        'Player A chooses B, Player B choose B': (total_happiness_B * 0.85 * 1.2, total_happiness_B * 1.1 * 1.2)
    }

    print('here are the updated values')
    for option in updated_game.items():
        print(option)

    total_game_theory = {
        'Player A chooses A, Player B choose A': total_happiness_A * 1.1 * 1.2 + (total_happiness_A * .85) * 1.2,
        'Player A chooses A, Player B choose B': total_happiness_A * 1.1 + total_happiness_B * 1.1,
        'Player A chooses B, Player B choose A': total_happiness_B * 0.85 + total_happiness_A * 0.85,
        'Player A chooses B, Player B choose B': total_happiness_B * 0.85 * 1.2 + total_happiness_B * 1.1 * 1.2
    }

    best_strat(total_game_theory)
