# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 05:27:37 2020

@author: 97250
"""
chinumber = int(input("enter number of children: "))
salnumber = int(input("enter your monthly salary:  "))
mil =input("militery serivce?\n for YES enter 'y' ,otherwise any other charecter:")
x = 20/100*salnumber
z = 30/100*salnumber
if salnumber <4000 and chinumber<4 :
    print("the morgage is not approved")
    
if mil == "y"and salnumber>=5000:
    print("the morgage is approved at the amount of :",x)
    
if chinumber >=4 and salnumber>= 4000 and salnumber<7500:
 print("the morgage is approved at the amount of :",x)


if salnumber>7500:
    print("the morgage is approved at the amount of :",z)
    
    
    
        
    


