# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:48:20 2021

@author: 97250
"""
def count(n, d):
    count = 0
    while (n > 0):
        if(n % 10 == d):
            count = count + 1
        n = n // 10
 
    return count

def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

x = int(input("enter integer : "))
y = countDigit(x)
while (x > 0):
    d = x%10
    count = count(x,d)
    print("the number %d appears %d times."%d%count)
    x = x//10
    