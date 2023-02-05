# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:07:42 2021

@author: 97250
"""

def build(a,b):
    if b==0:
        return 0
    #if b equal 0 return 0
    if b==1:
        return a%10
    #if be equal 1 we return the last digit of a 
    if b<10:
        return a%10*b 
    #if b is one digit return the last digit of a multiplied b
    return a%10 *b%10+10* build(a//10,b//10)
    
def main():
  print(build(1234,1001))
  print(build(1234,10))
  print(build(1234567890,101010))
    
main()    
