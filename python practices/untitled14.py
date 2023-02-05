# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:54:31 2021

@author: 97250
"""

def num_positive(num):
    if num < 10:
        return True
    return False
    
def same_digits(num):
    while num>9:
        digit= num%10
        S=num//10
        while S>0:
            dig2 =S%10
            if digit == dig2:
                return False
            S//=10
        num//=10
    return True

def 2dig_sub(num):
    while num>9:
        digit = num%10
        sec=num//10%10
        if digit - sec ==-1 or digit - sec==1:
            return False
        num//=10
    return True

def main(): 
    num=int(input("Enter positive integer (not less than 2 digits):"))
    if num_positive(num):
        print(num, "The number must be positive and more than 2 digits")
    else:
        if 2dig_sub(num) == True and same_digits(num)== True:
            print(num,"The number is WEll mixed.")
        else:
            print(num,"The number is NOT WEll mixed.") 