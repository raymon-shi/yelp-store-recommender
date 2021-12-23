import requests
from bs4 import BeautifulSoup
from PIL import Image
from urllib.request import urlopen
import random

from basic_functions import *


def scrappable_menus_list(yelp_top_list):
    scrap_menus = list()
    yelp_menu_url = 'https://www.yelp.com/menu/'
    # loop through all the top stores and their yelp websites
    for store in yelp_top_list:
        url = store['yelp_website']
        resp = requests.get(url)
        html = resp.text
        doc = BeautifulSoup(html, 'html.parser')
        # this is the tag of the 'full menu' button
        full_menu_button = doc.find(
            'div',
            class_='display--inline-block__373c0__2de_K margin-r2__373c0__1MwD- border-color--default__373c0__2oFDT')
        print('processed:', store['name'])

        # if the yelp_menu_url exists in this tag, then add it to the list of scrappable stores
        # the reason why i work with only the stores that have the yelp full menu feature is because these menus are significantly easier to scrape and they work on every store that has the similar full menu structure
        if yelp_menu_url in str(full_menu_button):
            print(store['name'], 'was added to scrappable menus list')
            scrap_menus.append(store['name'])

    return scrap_menus


def bring_up_menu(name_of_location, yelp_top_list):
    for store in yelp_top_list:
        # match the store of interest
        if store['name'] == name_of_location:
            url = store['yelp_website']
            resp = requests.get(url)
            html = resp.text
            doc = BeautifulSoup(html, 'html.parser')
            # specific location of the link, if it exists
            menu_link = doc.findAll('a', class_='css-1g3e5b2')[3]['href']
            # connect to the new url
            resp_menu = requests.get(menu_link)
            menu_html = resp_menu.text
            menu_doc = BeautifulSoup(menu_html, 'html.parser')

            # name of the menu items
            all_menu_item_names = menu_doc.findAll('h4')

            # price of the menu items
            all_menu_prices = menu_doc.findAll(
                'li', class_='menu-item-price-amount')

            menu_item_with_price = list()
            menu_item_names = list()
            menu_prices = list()

            print('this is the menu of:', name_of_location)

            # loop through the items and print the name and price
            for item_name, item_price in zip(all_menu_item_names, all_menu_prices):
                name_of_item = item_name.text.strip()
                price_of_item = item_price.text.strip()
                print(name_of_item, '--------------------------',
                      price_of_item)
                menu_item_with_price.append((name_of_item, price_of_item))
                menu_item_names.append(name_of_item)
                menu_prices.append(float(price_of_item.replace('$', '')))

            spending_money = input(
                'how much money do you want to spend? (float only): ')

            # find the average cost and average amount things you can by with x dollars
            average_item_cost = sum(menu_prices) / len(menu_prices)
            average_can_afford = float(spending_money) / average_item_cost

            print('the average cost of an item at this store is', average_item_cost,
                  'you can afford an average of', average_can_afford, 'items')


def request_pictures(name_of_store, yelp_top_list):
    for store in yelp_top_list:
        # match the store of interest
        if store['name'] == name_of_store:
            url = store['yelp_website']
            resp = requests.get(url)
            html = resp.text
            doc = BeautifulSoup(html, 'html.parser')

            # find the location of the source image
            tag_location = doc.find('a', class_='css-1fepc68')
            see_photo_link = 'https://www.yelp.com' + tag_location['href']
            photo_resp = requests.get(see_photo_link)
            photo_html = photo_resp.text
            photo_doc = BeautifulSoup(photo_html, 'html.parser')
            photo_tag_location = photo_doc.find_all('img', class_='photo-box-img')

            list_of_images = list()
            iter = 0

            # save the first 28 photos on the first page
            for photo_tag in photo_tag_location:
                iter = iter + 1
                print('storing photo for store:', store['name'], 'photo number:', iter)
                source_link = photo_tag['src']
                response = requests.get(source_link)
                picture = Image.open(urlopen(source_link))
                print(source_link)
                list_of_images.append(picture)

            # randomly show 5 photos from 1 to max (first photo is small and sucks)
            max_ran_num = len(list_of_images) - 1

            for iteration in range(5):
                list_of_images[random.randint(1, max_ran_num)].show()
