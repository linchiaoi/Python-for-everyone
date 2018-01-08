# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:05:20 2018

@author: ACER
"""
new_list = []

# The namings are really terrible, really hard to follow. 
# Grade C- for the variable names
# Grade A for the other stuff
reading0 = input('Please enter a file')
reading = open(reading0)


for line in reading:
    t = line.split(' ')
    for i in t:
        if i in new_list:
            continue
        else:
            # To add stuff to a list you use the append function
            new_list.append(i)
#print (new_list)
            
            
# When sorting, the list doesn't return anything. It is just sorted
new_list.sort()
print(new_list)

    