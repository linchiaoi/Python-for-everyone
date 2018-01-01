# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:05:35 2017

@author: ACER
"""


#subject=0
lines = 0

print('python egg.py')
#try:
#    data =input('please enter a name of file:') 
#   handel_data = open(data)
data =input('please enter a name of file:') 
handel_data = open(data)
                       
#except:
#    print ('file cannot be opened:', data)
 #   exit()
    
for lines in data:
    #subject = subject + line.count()
    lines = int(lines + 1)
print ('There were', lines, 'subject lines in', data)   
    
