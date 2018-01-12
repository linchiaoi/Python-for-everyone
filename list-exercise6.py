# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:27:34 2018

@author: ACER
"""

all_list = 0
while True:
    new_number = input('please enter a number:')
    if new_number == "done":
        break
    
    try:
        
        add_to_the_list = float(new_number)
        all_list.append(add_to_the_list)
        
    except:
        print('the input is not valid,please print a new number')
        
        
maximum = max(add_to_the_list)
minimum = min(add_to_the_list)
print ('Maximum:', maximum)
print ('Minimum:', minimum)
