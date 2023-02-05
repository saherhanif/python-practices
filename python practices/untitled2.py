# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:26:00 2021

@author: 97250
"""
def countOccurrances(n, d):
    count = 0
    while (n > 0):
        if(n % 10 == d):
            count = count + 1
        n = n // 10
 
    return count