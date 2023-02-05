# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:07:10 2021

@author: 97250
"""

def is_palindrom(s):
    if  not s:
        return True # if the list is empty return true
    if s[0]!=s[-1]: # if the first element of the list != the last element of the list return false
        return False
    return is_palindrom(s[1:-1]) # return the list and remove the first and the last element(that we already checked)



def main():
  ans ='y'
  while ans =='y': 
    s = str(input("enter numbers sapprated by commas :"))
    list = s.split(",")
    x = is_palindrom(s)
    if x == True:
        print("the list is a palindrom")
    else:
        print("this list isnt a palindrom")
    ans = str(input("try again? : (y/n) :"))
    if ans != 'y':
        print("finish!")
    

main()