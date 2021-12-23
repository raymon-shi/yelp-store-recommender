def miles_to_meters(miles):
    return int(float(miles) * 1609.0)


def meters_to_miles(meters):
    return meters / 1609.0


def dollar_sign_all(dollar_sign_amount):
    if dollar_sign_amount == '1':
        return '1'
    elif dollar_sign_amount == '2':
        return '1, 2'
    elif dollar_sign_amount == '3':
        return '1, 2, 3'
    elif dollar_sign_amount == '4':
        return '1, 2, 3, 4'
    else:
        print('enter a valid dollar sign amount')


def dollar_sign_convert(string_dollar):
    if string_dollar == '$':
        return 1.0
    elif string_dollar == '$$':
        return 2.0
    elif string_dollar == '$$$':
        return 3.0
    elif string_dollar == '$$$$':
        return 4.0
    else:
        print('enter a valid dollar sign amount')


def happiness(star_rating, review_number, dollar_amount):
    return (star_rating * 20.0) + (review_number * 0.1) - (dollar_amount * 25.0)


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


##########################################################################
##########################################################################
##########################################################################

yelp_businesses_search_url = 'https://api.yelp.com/v3/businesses/search'
yelp_header = {'Authorization': 'Bearer ' + yelp_api_key}
