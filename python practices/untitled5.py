# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 03:11:41 2020

@author: 97250
"""

thenumber =int(input("enter a positive 4-digits number:"))

if 0<thenumber<1000 or thenumber>9999 :
    print(thenumber,"is not a 4-digits number, bye bye")
    
firstindex = thenumber//1000
secondindex = thenumber//100-firstindex*10
thirdindex = thenumber//10-firstindex*100-secondindex*10
forthindex = thenumber%10

d1= secondindex-firstindex
d2= thirdindex-secondindex
d3= forthindex-thirdindex
if thenumber<0:
    print("this is a negative number, bye bye")
if d1 ==  d2 == d3 and firstindex < secondindex:
    print("increasing arthimetic sequence(from left to right)")

if d1 == d2 == d3 and firstindex > secondindex:
    print("decreasing arthimetic sequence(from left to right)")
     
if firstindex < secondindex and secondindex <= thirdindex and thirdindex <= forthindex and d1 != d2 :
    print("ascending sequence(from left to right)")
 
if  firstindex > secondindex and secondindex >= thirdindex and thirdindex >= forthindex and d1!= d2:
    print("descending sequence(from left to right)") 
    
if  firstindex==secondindex == thirdindex  == forthindex:
    print("all digits are the same") 
 

    
    
    