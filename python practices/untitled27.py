# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:03:22 2021

@author: 97250
"""

def check_letters(str1):
    
    if str1=="":
        return True
#if the string is an empty
    return ((64<ord(str1[0]) and ord(str1[0])<91) or (96<ord(str1[0]) and ord(str1[0])<123)) and check_letters(str1[1:])
#every time we check if the ord of the first element is between 64 and 91 or between 96 and 123 according to asci art 

def main():
    print(check_letters("429TTY4967295"))
    print(check_letters("ABCabcYY"))
    print(check_letters(""))
main()    
