#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:15:31 2022

@author: xiaoyuzhang
"""


import requests
from bs4 import BeautifulSoup as bs
import os

url = 'https://www.airbnb.co.uk/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2020-11-01&checkout=2020-11-08&source=structured_search_input_header&search_type=autocomplete_click'


r = requests.get(url)
soup = bs(r.text,'html.parser')

#print(soup.title.text)

images = soup.find_all('img')
#print(images)

for image in images:
    #print(image['src'])
    name = image['alt']
    link = image['src']
    #print(name,link)
    with open(name + '.jpg', 'wb') as f:
        im = requests.get(link)
        f.write(im.content)