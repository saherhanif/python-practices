# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 01:59:11 2020

@author: 97250
"""

weight = int(input("enter weight(in kg)"))
height = int(input("enter height(in cm)"))

height = height/100

bmi = weight/(height**2)

if bmi<18.5:
 print("under weight")

if bmi>=18.5 and bmi<25:
 print("normal weight")
      
if bmi>=25 and bmi<30:    
 print("increased weight")  
    
if bmi>=30 and bmi<40:    
 print("obese")  
   
if bmi>=40:    
 print("very high obese")  
     
        
    