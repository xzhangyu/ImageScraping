#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:54:59 2022

@author: xiaoyuzhang
"""
import re

abc="Antrostomus noctitherus,Tringa guttifer,Pitta megarhyncha,Necrosyrtes monachus,Notiomystis cincta,Apteryx mantelli,Gallicolumba platenae,Aythya innotata"
birdNameList=abc.split(',')
print(birdNameList)

for i in birdNameList:
    print(i)
#print(' '.join('"{}"'.format(word) for word in abc.split(' ')))
