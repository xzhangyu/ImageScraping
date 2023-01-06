#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 18:10:42 2022

@author: xiaoyuzhang
"""
# =============================================================================
# 批量生成网站的标题和网址
# =============================================================================

import requests        #导入requests包
from bs4 import BeautifulSoup as bs
import re
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}


def printInfo(url):
    for i in url:
        html = requests.get(i,headers=header)
        html.encoding='utf-8'
        soup=bs(html.text,'lxml')
        title = soup.find('title')
        print(title.text,"\n",i,"\n")
# =============================================================================
#         if title == True:
#             print(title.text,"\n",i,"\n")
#         else:
#             "There is no title element of this page"
#             continue
# =============================================================================
printInfo(
    ["https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception",
     "http://c.biancheng.net/view/4599.html",
     "https://www.runoob.com/python/python-exceptions.html",
     "https://support.apple.com/en-gb/guide/numbers/tan0403655e1/mac",
     "https://www.zhihu.com/question/19696149",
     "https://www.animaapp.com/blog/design-to-code/how-to-export-figma-to-html/",
     "",
     "",
     "",
     "",])

