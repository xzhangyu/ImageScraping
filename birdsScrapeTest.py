# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Created in May.17
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.expected_conditions import presence_of_element_located
#from bs4 import BeautifulSoup
import requests
import os
from selenium.common.exceptions import NoSuchElementException


#Set up the bird name list
abc="Antrostomus noctitherus,Tringa guttifer,Pitta megarhyncha,Necrosyrtes monachus,Notiomystis cincta,Apteryx mantelli,Gallicolumba platenae,Aythya innotata,Alopecoenas erythropterus,Artisornis moreaui,Pithecophaga jefferyi,Strigops habroptila,Houbaropsis bengalensis,Pternistis ochropectus,Nemosia rourei,Antilophia bokermanni,Thalasseus bernsteini,Celeus obrieni,Ara ararauna,Tachyeres leucocephalus,Clangula hyemalis,Diomedea exulans,Pseudibis davisoni,Ardea insignis,Mergus octosetaceus,Podiceps gallardoi,Calidris pygmaea,Spheniscus demersus,Terpsiphone corvina,Eriocnemis nigrivestis,Pomarea nigra,Lanius newtoni,Alauda razae,Heteromirafra archeri,Turdus helleri,Atlapetes pallidiceps,Geospiza heliobates,Palmeria dolei,Cinclodes palliatus,Falco cherrug,Gyps africanus,Gyps bengalensis,Gyps indicus,Sarcogyps calvus,Bubo scandiacus"
#abc="Antrostomus noctitherus,Tringa guttifer,Pitta megarhyncha,Necrosyrtes monachus,Notiomystis cincta"
birdNameList=abc.split(',')

#Set up image-saving path
try:
    os.mkdir(os.path.join(os.getcwd(),'birdsImages'))
except:
    print("an error occurs")
os.chdir(os.path.join(os.getcwd(),'birdsImages'))

#Set up Chromedriver
s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)
    
#Explicit waiting time
wait = WebDriverWait(driver, 10)
    
#Run a loop to download one picture for each bird 
for i in birdNameList:
    
    #Input search page
    driver.get("https://ebird.org/explore")
    
    #Find search bar
    inputSpot = driver.find_element(By.ID,'Suggest-0')
    
    #Input name of the bird into search bar
    name = i
    inputSpot.send_keys(name)
    sleep(1.5)#enter after 5 seconds
    
    #Check if the bird exist in the pop-up search result
    textContent = driver.find_elements(By.CLASS_NAME, "SciName")
    for value in textContent:
        check = value.text
    if i == check:
        #print("This species exists in website")
        inputSpot.send_keys(Keys.ENTER)
        
        #Enter the species info page
        driver.get(driver.current_url)
        #Get the picture element
        sleep(0.5)
        
        #Get the current state of the species
        state = driver.find_elements(By.CLASS_NAME, "Badge-label")
        for value in state:
            survivalState = value.text
        #print(survivalState)
        
        #Test if the state is endangered or critically endangered
        if survivalState == "EN" or survivalState == "CR":
            try:
                doesElementExist = driver.find_element(By.CSS_SELECTOR,'div.MediaThumbnail.Media--playButton>img').is_displayed()
            except NoSuchElementException:
                print("Cannot find the picture of "+i+"Please download it yourself.")
                continue
            #print(doesElementExist)
            url = driver.find_element(By.CSS_SELECTOR,'div.MediaThumbnail.Media--playButton>img').get_attribute('src')
            #sleep(1.5)
                
            #Saving pictures
            r = requests.get(url)
            with open(name+'.jpg', 'wb') as f:
                f.write(r.content)
            print(name+' downloaded!')
            
        elif survivalState != "EN" or survivalState != "CR":
            print("This species is not endangered or critically endangered")
    else:
        print("This species cannot be found here")
driver.quit()
print('All Downloaded')


#performance issues