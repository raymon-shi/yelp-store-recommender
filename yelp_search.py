from basic_functions import *
import requests

# important global variables
term = input('Enter the type of establishment youre looking for: ')
limit = 10
radius_in_miles = input(
    'Enter the furthest distance you are willing to go in miles: ')
radius_in_meters = miles_to_meters(radius_in_miles)
location = input('Enter the your location (Address or Zip Code): ')
price = input(
    'Enter the maximum dollar sign amount you are willing to spend (max of 4): ')
price_input_readjusted = dollar_sign_all(price)


def yelp_search_start():
    # the initial search for the yelp top 10 list
    yelp_search_parameters = {
        'term': term,
        'limit': limit,
        'radius': radius_in_meters,
        'location': location,
        'price': price_input_readjusted
    }

    resp = requests.get(url=yelp_businesses_search_url,
                        params=yelp_search_parameters, headers=yelp_header)

    yelp_search_return = resp.json()

    return yelp_search_return


def yelp_print_entires(yelp_top_10_list):
    # prints each store dictionary out
    for store in yelp_top_10_list:
        print('here is one of the top stores:', store, '\n')


def other_store_search(current_store, compared_store):
    # the search done when comparing the current store with every other store
    yelp_search_params = {
        'term': compared_store['name'],
        'location': current_store['location'],
        'limit': limit,
        'radius': radius_in_meters,
        'price': price_input_readjusted
    }

    resp = requests.get(url=yelp_businesses_search_url,
                        params=yelp_search_params, headers=yelp_header)

    yelp_search_return_dict = resp.json()

    return yelp_search_return_dict
