#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:05:18 2022

@author: xiaoyuzhang
"""
import requests
from bs4 import BeautifulSoup
import time

url = 'https://sc.chinaz.com/tupian/beijingtupian.html'
resp = requests.get(url)
resp.encoding='utf-8'
#print(resp.text)


bs = BeautifulSoup(resp.text,'html.parser')
a_list = bs.find('div',{'id':'container'}).find_all('p')
#pp = a_list.find("a")
#print(a_list)
for it in a_list:
    child_page = it.find("a")
    url2 = 'http:' + child_page.get('href')
    #获取子页面内容
    resp2 = requests.get(url2)
    resp2.encoding='utf-8'
    #print(resp2.text)
    img = BeautifulSoup(resp2.text,'html.parser')
    img_link = img.find('div',{'class':'imga'}).find('img')
    #print('http:' + img_link.get('src'))
    img_src = 'http:' + img_link.get('src')


    #下载图片
    resp3 = requests.get(img_src)
    img_name = img_src.split('/')[-1] #对照片进行命名 用照片链接的后几位
    with open("images/" + img_name,mode='wb') as f:
        f.write(resp3.content)
    time.sleep(1)


    print('over!',img_name)
print('over!!')















