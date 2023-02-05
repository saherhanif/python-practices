# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:06:10 2021

@author: 97250
"""

def recursive_has_prefix(str1,prefix):
   if not str1 and prefix: # basically if str1 is smaller than prefix return false
       return False
   if not prefix: # if we get to an empty prefix then the answer is true
       return True 
   if str1[0]==prefix[0]: # compare the first character of each string
       return recursive_has_prefix(str1[1:], prefix[1:]) # recursive call for substrings from range [1...]
   return False # if we get here then the comparison condition failed therefore return false

def main():
    isPrefix = True
    while isPrefix:
        str1 = input("Please enter a string: ")
        pref = input("Please enter a prefix string: ")
        isPrefix = recursive_has_prefix(str1, pref)
        if isPrefix:
            print("The text has the prefix")
        else:
            print("No prefix")
    print()
main()
