# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:05:20 2018

@author: ACER
"""
new_list = []


reading0 = input('Please enter a file')
reading = open(reading0)


for line in reading:
    t = line.split(' ')
    for i in t:
        if i in new_list:
            continue
        else:
            new_list.append(i)
#print (new_list)
            
            

new_list.sort()
print(new_list)

    