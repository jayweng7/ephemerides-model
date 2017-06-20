# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 18:07:47 2017

@author: jaywe
"""

import numpy as np
import re

file = open("earth.txt", "r")
start = '$$SOE'
end = '$$EOE'

while (start not in file.readline()):
    file.readline()
    
#==============================================================================
# print(file.readline())
# print(file.readline())
#==============================================================================

#==============================================================================
# s = file.readline()
# 
# s1,s2,s3,s4,s5 = s.split(", ")
# 
#  
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# 
# s5 = re.sub(',', '', s5)
# print(s5)
#==============================================================================

ephemeris = np.empty([31, 3])
i=0

while True:
     s = file.readline()
     if (end in s):
         break
     s1,s2,s3,s4,s5 = s.split(", ")
     s5 = re.sub(',', '', s5)
     ephemeris[i][0] = s3
     #print(s3)
     #print(ephemeris[i][0])
     ephemeris[i][1] = s4
     ephemeris[i][2] = s5
     i += 1

     
for i in range(1, 31):
     print(ephemeris[i][0])
     print(ephemeris[i][1])
     print(ephemeris[i][2])
    