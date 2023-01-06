#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 00:00:13 2022

@author: xiaoyuzhang
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from bs4 import BeautifulSoup
import requests

s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s) 
wait = WebDriverWait(driver, 10)
driver.get("https://ebird.org/explore")
inputSpot = driver.find_element(By.ID,'Suggest-0')
name = "Antrostomus noctitherus"
inputSpot.send_keys(name)
sleep(5)#enter after 5 seconds
inputSpot.send_keys(Keys.ENTER)
#driver.find_element(By.ID,'Suggest-suggestion-0').click()
#print(driver.current_url)
driver.get(driver.current_url)
url = driver.find_element(By.CSS_SELECTOR,'div.MediaThumbnail.Media--playButton>img').get_attribute('src')
print(url)
sleep(3)
driver.quit()
r = requests.get(url)
with open(name+'.jpg', 'wb') as f:
    f.write(r.content)
print('over!')

#制作array
#写for loop
#写writing+name
#rearrange code
#查询反复打开又exit driver是否会非常耗能

























