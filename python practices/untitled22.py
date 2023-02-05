# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:22:45 2021

@author: 97250
"""
"""
x = "Welcome to the Lab no ELEVEN in Computer Science."
"""
def find_max_appearnce(x):
    y = [0]*26 # will use this array to count every letters apearnce
    x = x.lower()
    
    for i in range(len(x)): # this loop will check if its a letter or a charcter and count the appearnce of every letter
       if x[i]>='a' and x[i]<='z':
        index =ord(x[i]) - ord('a')
        y[index]+=1
    
    mx=0
    maxchar = ''
    
    for i in range(len(y)):  # find the max number in the y array witch is the number with the most appearnce
        if y[i]>mx:
            mx = y[i]
            maxchar = chr(i+ord('a'))
    if mx == 0 :
        print(-1)
    else:
     print("the letter with the most appearnce is : ",maxchar)


        
def main ():
    x=""
    while x != "quit" :
        x = str(input("enter your string : "))
        x = x.lower()
        if x== "quit":
            print("Thank you for exploring strings and complexity")
        else:
         find_max_appearnce(x)    
main()

        