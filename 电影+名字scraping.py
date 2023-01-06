#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 23:37:10 2022

@author: xiaoyuzhang
"""

# =============================================================================
# 此练习的关键在于学会观察要scrape的内容的tag
# 学习用beautifulsoup去access想要的层级以及tag
# =============================================================================

import requests
from bs4 import BeautifulSoup as bs
import os

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
    except:
        print("an error occurs")
    os.chdir(os.path.join(os.getcwd(),folder))
    
    
    r = requests.get(url)
    r.encoding='utf-8'
    soup = bs(r.text,'html.parser')
    
    #print(soup.title.text)
    images = soup.find_all('div',class_="el-card__body")
    #print(images)
    

    for image in images:
        #print(image['src'])
        name = image.h2.text
        link = image.img['src']
        #print(name,link)


        with open(name + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing:',name)
    print('over!!')
            
            
imagedown('https://ssr1.scrape.center/','MovieNames')






























