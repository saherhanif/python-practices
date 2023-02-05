# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:58:20 2021

@author: 97250
"""

def rstr2u(str):
  if len(str)==0:
      return 0
  #if the string is empty
  if str[0]=="-": #if the number is negative remove the negative sign
      str=str[1:]  
      return ((ord(str[-1]) - ord('0')) + 10 * rstr2u(str[:-1]))*-1# *-1 because its a negative number
     
  
  else:
   return (ord(str[-1]) - ord('0')) + 10 * rstr2u(str[:-1])

def main():
   str= input("enter a string: ")
   print("the str is : ",str)
   print("the integer number is", rstr2u(str)) 
main()    
