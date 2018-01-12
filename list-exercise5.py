# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 19:55:55 2018

@author: ACER
"""


print('python fromcount.py')
file = input('please enter a file name:')

reading_file = open (file)

count = 0
for line in reading_file:
    if line.startswith('From'):
        new_line=line.split(' ')
        print (new_line [1])
        
        count = count +1
print ('There were' , count, 'lines in the file with From as the first word')        

        
    
#except:    print('the name of file in invalid, please enter a valid name!')
    
