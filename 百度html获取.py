#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:49:47 2022

@author: xiaoyuzhang
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s) 
wait = WebDriverWait(driver, 10)
driver.get("https://www.baidu.com/")
driver.find_element_by_id('kw').send_keys("Python" + Keys.RETURN)