# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:03:43 2021

@author: 97250
"""

def input_list(n):
    ls = []
    for i in range(n):
        x = float(input("%d . enter time:- "%(i+1)))
        ls.append(x)
    return ls

def my_Avg(ls):
    return sum(ls) / len(ls)

def under_avg(ls):
    count =0
    avg = my_Avg(ls)
    for i in range(len(ls)):
        if ls[i] < avg:
            count+=1
        
    return count

def main():
    n = int(input("enter the number of runners :- "))
    a = input_list(n)
    avg = my_Avg(a)
    count = under_avg(a)
    print("time average is :- %.2f"%avg)
    print("the number of runners , running below average is :- ",count)

main()
"""
    17.4	18.1	17.4	19.2	14.4	30.6	19.2
13.99	13.99	13.99	13.99	13.99	13.99	13.99
"""    