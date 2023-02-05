# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:41:35 2021

@author: 97250
"""

def count_char(s,y): # the function will take a string and an empty array filled with 0  (size 127)
    if len(s)>0: # while the string is not emprty count every letter in the right place 
        x=s[0]
        index= ord(x)
        y[index]+=1 
        return count_char(s[1:], y) # after counting the first letter ...return the string from the second letter 
   
    return y 


def Combination(s1,s2,s3):
    count1 = [0]*127 # an empty array to count the appearnce of every letter in s1 
    count2 = [0]*127 # an empty array to  count the apearnce of evey letter in s2
    count3 = [0]*127 # an empty array to  count the appearnce of every letter in s3 
    count1 = count_char(s1,count1)
    count2 = count_char(s2,count2)
    count3 = count_char(s3,count3)
    count4 = [0]*127 # we will save the sun of s1 ,s2 arrays in count 4
    
    for i in range(len(count1)): # the sum of s1 s2 letter appearnce
        count4[i]=count1[i]+count2[i]
    
    if count3 == count4: # if count4 witch is the sun of s1 ,s2 letters appearnce == count3 return true 
        return True
    return False

"""
s="abcdef"
print(Combination("abc","def", "abcdef"))
"""
def main():
    s1="TTTT"
    s2="X"
    s3="XXXXX"
    if Combination(s1, s2, s3)==True:
        print("%s is a combination of %s and %s"%(s3,s2,s1))
    else:
        print("%s is not a combination of %s and %s"%(s3,s2,s1))        

main()
    