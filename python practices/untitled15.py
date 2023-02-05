# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:01:29 2021

@author: 97250
"""


def check_same_digits(num):
    while num> 9:
        digit= num%10
        S=num//10
        while S>0:
            dig2 =S%10
            if digit == dig2:
                return False
            S//=10
        num//=10
    return True

def check_2dig_sub(num):
    while num>9:
        digit = num%10
        sec=num//10%10
        if digit - sec ==-1 or digit - sec==1:
            return False
        num//=10
    return True

def main(): 
    num=int(input("Enter positive integer (not less than 2 digits):"))
    if num < 10:
        print(num, "The number must be positive and more than 2 digits")
    else:
        if check_2dig_sub(num) == True and check_same_digits(num)== True:
            print(num,"The number is WEll mixed.")
        else:
            print(num,"The number is NOT WEll mixed.") 