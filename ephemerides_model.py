# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:29:08 2017

@author: jaywe
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import re

file = open("earth_1year_day.txt", "r")
start = '$$SOE'
end = '$$EOE'

s = file.readline()
while (start not in s):
    s = file.readline()
    
ephemeris = np.empty([366, 3])
i=0


while True:
     s = file.readline()
     if (end in s):
         break
     s1,s2,s3,s4,s5 = s.split(", ")
     s5 = re.sub(',', '', s5)
     ephemeris[i][0] = s3
     ephemeris[i][1] = s4
     ephemeris[i][2] = s5
     i += 1

minmax = 1000000000

fig = plt.figure()
ax = p3.Axes3D(fig)


#==============================================================================
# data = np.empty([10, 3])
# for i in range(1, 10):
#     for j in range(1, 3):
#         data[i][j] = np.random.randint(0, 10)
#         
# print(data)
#==============================================================================

def func(num):
    ax.cla()
    
    ax.autoscale(False, axis='both')
    ax.autoscale(False, axis='z')

    ax.set_xbound(-minmax, minmax)
    ax.set_ybound(-minmax, minmax)
    ax.set_zbound(-minmax/100, minmax/100)

    ax.scatter3D(0,0,0,zdir='z')
    ax.scatter3D(ephemeris[num][0], ephemeris[num][1], ephemeris[num][2])  

anim = animation.FuncAnimation(fig, func, 366, interval=1, blit=False)


plt.show()