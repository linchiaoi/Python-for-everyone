# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:47:28 2018

@author: ACER
"""

new_list = []

# The namings are really terrible, really hard to follow. 
# Grade C- for the variable names
# Grade A for the other stuff
raw_input = input('Please enter a file')
reading = open(raw_input)


for line in reading:
    the_sentance = line.split(' ')
    for the_words in the_sentance:
        if the_words in new_list:
            continue
        else:
            # To add stuff to a list you use the append function
            new_list.append(the_words)
#print (new_list)
            
            
# When sorting, the list doesn't return anything. It is just sorted
new_list.sort()
print(new_list)