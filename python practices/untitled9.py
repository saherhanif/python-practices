# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:39:05 2020

@author: 97250
"""
import math 
import random

def longestSubarray(all_players):
  number_of_players=int(input("Enter the players number: "))
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