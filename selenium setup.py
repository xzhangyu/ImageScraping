# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s) 
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit() 