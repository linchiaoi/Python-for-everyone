# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:53:28 2017

@author: ACER
"""

data = open('romeo.txt')
list = ['0']
for line in data:
    words = line.split()
    print (words)
    if words not in list:
        list.append(words)
list.sort()
print (list)
