# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:03:54 2020

@author: 97250
"""
import math 
import random

number_of_players=int(input("Enter the players number: "))
all_players=[]
a=[]
p=[]
def play(number_of_players):

def print_ticketarrey(number_of_players):
   
   for i in range(number_of_players):
     a.clear()
     for h in range(10):
       random_number=random.randint(1,100)
       a.append(random_number)
     all_players.append(a.copy())
     print("player", i+1 ,"ticket:",all_players[i] ) 
   
   

global j

def longestSubarray(all_players):
 max=1 
 for i in range(len(all_players)):
    for j in range(len(all_players[i])-1):
       count=0
       first=all_players[i][j]
       second=all_players[i][j+1]
       while second>first and j<len(all_players[i])-3:
           count+=1
           j+=1
           first=all_players[i][j]
           second=all_players[i][j+1]
           
           if max<count:
              max=count
              






    
    
    