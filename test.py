import requests
from bs4 import BeautifulSoup
from PIL import Image
from urllib.request import urlopen
import random

# yelp_url = 'https://www.yelp.com/biz/beilers-donuts-philadelphia'
# resp = requests.get(yelp_url)
# html = resp.text
# doc = BeautifulSoup(html, 'html.parser')
# tag_location = doc.find('a', class_='css-1fepc68')
# see_photo_link = 'https://www.yelp.com' + tag_location['href']
# photo_resp = requests.get(see_photo_link)
# photo_html = photo_resp.text
# photo_doc = BeautifulSoup(photo_html, 'html.parser')
# photo_tag_location = photo_doc.find_all('img', class_='photo-box-img')
# list_of_images = list()
# iter = 0
# for photo_tag in photo_tag_location:
#     iter = iter + 1
#     print('storing photo', iter)
#     source_link = photo_tag['src']
#     response = requests.get(source_link)
#     picture = Image.open(urlopen(source_link))
#     print(source_link)
#     list_of_images.append(picture)
#     # picture.show()
#
# for iteration in range(5):
#     list_of_images[random.randint(1, 27)].show()




