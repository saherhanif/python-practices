# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:26:48 2021

@author: 97250
"""
"""
n =7
a = [5,3,2,1,6,8,7]
x = 4
"""
def input_list(n):
    ls = []
    for i in range(n):
        x = int(input("%d . enter an integer:- "%(i+1)))
        ls.append(x)
    return ls





def create_new_list(a,x):
    b = []
    c = a.copy()
    for num in list(a):
        if num < x:
            b.append(num)
            c.remove(num)
    b.extend(c)
    return b


 
def main():
    n=7
    a=input_list(n)
    
    x=int(input("enter x : "))
    y =create_new_list(a,x)
    print("the original list is :- ",a)
    print("the new list is : - ",y)


main()