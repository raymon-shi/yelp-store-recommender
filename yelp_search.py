from basic_functions import *
import requests


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


def yelp_result_list_maker(results_dict):
    result_list = list()
    # sometimes the yelp api decides to return None for some reason, not entirely sure....
    if 'businesses' in results_dict.keys():
        # look at all the business attributes
        for business in results_dict['businesses']:
            # create a new dictioanry with business details that I find are important
            results_business_details = {
                'name': business['name'],
                'phone_number': business['phone'],
                'yelp_website': business['url'],
                'business_id': business['id'],
                'dollar_amount': business['price'],
                'star_rating': business['rating'],
                'review_number': business['review_count'],
                'location': business['location']['address1'] + ' ' + business['location']['city'] + ' ' +
                            business['location']['state'] + ' ' + business['location']['zip_code'],
                'distance': meters_to_miles(float(business['distance'])),
                'happiness': happiness(float(business['rating']), float(business['review_count']),
                                       dollar_sign_convert(business['price']))
            }
            # add it to a resulting list, creating a list of dictionaries, where each dictionary represents a store
            result_list.append(results_business_details)

    return result_list


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
