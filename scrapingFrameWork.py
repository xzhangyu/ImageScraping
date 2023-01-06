#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:50:33 2022

@author: xiaoyuzhang
"""

import requests
from bs4 import BeautifulSoup as bs
import os

#url = 'https://www.airbnb.co.uk/s/Ljubljana--Slovenia/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Ljubljana%2C%20Slovenia&place_id=ChIJ0YaYlvUxZUcRIOw_ghz4AAQ&checkin=2020-11-01&checkout=2020-11-08&source=structured_search_input_header&search_type=autocomplete_click'


def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
    except:
        print("an error occurs")
    os.chdir(os.path.join(os.getcwd(),folder))
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
            print('Writing:',name)
            
imagedown('https://www.airbnb.co.uk/s/London/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=London%2C%20UK&source=structured_search_input_header&search_type=autocomplete_click&flexible_trip_lengths%5B%5D=one_week&place_id=ChIJdd4hrwug2EcRmSrV3Vo6llI&date_picker_type=calendar&checkin=2022-05-15&checkout=2022-05-22','London')


#How to Scrape and Download ALL images from a webpage with Python：https://www.youtube.com/watch?v=stIxEKR7o-c
