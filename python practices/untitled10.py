# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:21:55 2020

@author: 97250
"""

number = int(input("Enter a number "))

def counter(number):
 count = 0
 while (number > 0):
  number = number//10
  count = count + 1
 print ("Total number of digits : ",count)
 return count


def lastdigit(number,count):
    for i in range(count-1):
        x = number//10**(count-1)
    
    return x


def newnumber(number,y):
    z = number - y*(10**(count-1))
    z = z*10
    return z


count = counter(number)
y = lastdigit(number, count)
z = newnumber(number,y)  
print(count)
print(z)
print(y)

number_of_elements = int(input("enter number of elements: "))
a=[]
for i in range(number_of_elements):
    
    w = input("enter element :")
    a.append(w)
 
    """
    original = [123456789402]
    rotated = [234567894021]
    size_array = [3,1,5,3]
  if 0 is the second number ?
  """



        

    