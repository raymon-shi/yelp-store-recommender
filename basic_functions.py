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


##########################################################################
##########################################################################
##########################################################################

# yelp api keys
client_id = 'ENTER_CLIENT_ID'
yelp_api_key = 'ENTER_YELP_API_KEY'

# in case of emergency, use other keys
yelp_api_key_2 = ''
yelp_api_key_3 = ''

yelp_businesses_search_url = 'https://api.yelp.com/v3/businesses/search'
yelp_header = {'Authorization': 'Bearer ' + yelp_api_key}

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
