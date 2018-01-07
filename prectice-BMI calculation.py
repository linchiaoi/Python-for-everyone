# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:18:50 2018

@author: ACER
"""

#practice: BMI calculation
weight = input('please enter your body weight(kg):')
height = input('please enter your height(cm)')

try:

    w = float(weight)
    h = float(height)/100
    
except:
    print ('please enter a valid number')

BMI = w/h/h
if BMI < 18.5:
    comment= 'underweight'
    
elif BMI >= 18.5 and BMI <= 24.9:
    comment = "Normal weight"
    
elif BMI >= 25 and BMI <=29.9:
    comment = 'Overweight'
    
elif BMI >=30:
    comment = 'obese'
    
print ('Your BMI is:', BMI)
print ('You are', comment)