# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 20:46:59 2017

@author: ACER
"""

data = input("enter a file name:")
handle_data= open(data)
new_line = 0
count = 0
for line in handle_data:
    if line.startswith('X-DSPAM-Confidence:'):
        b= line.find('X-DSPAM-Confidence:')
        number = float(line[b+19:])
        new_line = new_line + number
        count = count + 1
average = float(new_line/count)
print ("Average spam confidence:", average)