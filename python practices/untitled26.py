# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:43:51 2021

@author: 97250
"""

def length_of_string(s):
    if s == '': # if the strint is empty return 0 ..and if at some point became empty then add 0 to our total
        return 0
    else :
        return 1 + length_of_string(s[1:]) # if the the string isnt empty then count 1 and add to it the recursive call [1...]
  
def main():
    text = "Experimental text to test recursive function."
    print("Length of string:\n%s\n is %d."% (text,length_of_string(text)))
main()
