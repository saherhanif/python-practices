# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:07:31 2021

@author: 97250
"""
"""
x = [[5,	4,	3,	2,	1],
[0,	9,	8,	7,	6],
[5,	4,	3,	2,	1],
[0,	9,	8,	7,	6],
[5,	4,	3,	2,	1]]

x = [[2,4,3,2,5,],
[0,3,8,7,6],
[5,4,4,2,1],
[5,	4,	3,	2,1]]

x = [[1]]

x= [[2,	4,	3,	2,	5],
[0,	3,	8,	7,	6],
[5,	4,	4,	2,	1],
[0,	9,	8,	0,	6],
[5,	4,	3,	2,	1]]
"""

def is_extreme(x):
    y=[]
    c=[]
    for i in range(len(x)):
        for j in range(len(x[i])):
            if (i == j):
               y.append(x[i][j])
    for i in range(len(x)):
        for j in range(len(x[i])):
            if ((i + j) == (len(x) - 1)):
                c.append(x[i][j])
    
    count = 0
    for i in range(len(c)):
        if y[i] <= c[i]:
            count += 1
    
    if count == len(y):
        return True
    else:
        return False




def main():
    x = [[5,4,3,2,1],
    [0,9,8,7,6],
    [5,4,3,2,1],
    [0,9,8,7,6],
    [5,4,3,2,1]]
    
    y = [[2,4,3,2,5,],
    [0,3,8,7,6],
    [5,4,4,2,1],
    [5,4,3,2,1]]
    
    z = [[1]]
    
    c= [[2,4,3,2,5],
    [0,3,8,7,6],
    [5,4,4,2,1],
    [0,9,8,0,6],
    [5,4,3,2,1]]
    print(x)
    print(is_extreme(x))
    print(y)
    print(is_extreme(y))
    print(z)
    print(is_extreme(z))
    print(c)
    print(is_extreme(c))
    
main()