# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:35:04 2021

@author: 97250
"""
import math

def height(t,v,a):
    a = deg2rad(a)
    vy = v* math.sin(a)
    h = vy*t-(9.81*(t**2))/2
    return h


    
def horizontal(t,v,a):
    a= math.radians(a)
    vx = v* math.cos(a)
    s= vx*t
    return s

def deg2rad(a):
    return math.radians(a)

def main():
    while True:
        v , a = input("enter v(0-100)m/s and a(0-90 degrees): ").split(',')
        a = float(a)
        v = float(v)
        t= float(0.1)
        
        if v > 100 or v< 0 or a<0 or a>90 :
            print("finish!")
            break
        else:
            h = height(t, v, a)
            s = horizontal(t, v, a)
            print("time = %.1f"%t,"s = %.2f"%s,"H = %.2f"%h )
            while h >=0 :
              t+=0.1
              h = height(t, v, a)
              s = horizontal(t, v, a)
              print("time = %.1f"%t,"s = %.2f" %s,"H = %.2f"%h )
            print("fallen!")


main()
  



      
"""


t =0.1 
v =12.5 
a = 45
a = math.radians(a)
print(height(t, v, a))
print(horizontal(t, v, a))
"""