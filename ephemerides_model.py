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

class planet():
    start = '$$SOE'
    end = '$$EOE'
    
    def __init__(self, name):
        self.name = name
    
    def getData(self, filename):
        file = open(filename)
        s = file.readline()
        while (self.start not in s):
            s = file.readline()
            
        ephemeris = np.empty([4750, 3])
        i = 0
        
        while True:
            s = file.readline()
            if (self.end in s):
                break
            s1,s2,s3,s4,s5 = s.split(", ")
            s5 = re.sub(',', '', s5)
            ephemeris[i][0] = s3
            ephemeris[i][1] = s4
            ephemeris[i][2] = s5
            i += 1
        
        return ephemeris
        
#==============================================================================
# file = open("earth_1year_day.txt", "r")
# start = '$$SOE'
# end = '$$EOE'
# 
# s = file.readline()
# while (start not in s):
#     s = file.readline()
#     
# ephemeris = np.empty([366, 3])
# i=0
# 
# 
# while True:
#      s = file.readline()
#      if (end in s):
#          break
#      s1,s2,s3,s4,s5 = s.split(", ")
#      s5 = re.sub(',', '', s5)
#      ephemeris[i][0] = s3
#      ephemeris[i][1] = s4
#      ephemeris[i][2] = s5
#      i += 1
#==============================================================================
#ephemerides = []

planets = []

mercury = planet
venus = planet
earth = planet
mars = planet
jupiter = planet
saturn = planet
uranus = planet
neptune = planet
pluto = planet

ephemeris_m1 = mercury.getData(mercury, 'mercury.txt')
ephemeris_v = venus.getData(venus, 'venus.txt')
ephemeris_e = earth.getData(earth, 'earth.txt')
ephemeris_m = mars.getData(mars, 'mars.txt')
ephemeris_j = jupiter.getData(jupiter, 'jupiter.txt')
ephemeris_s = saturn.getData(saturn, 'saturn.txt')
ephemeris_u = uranus.getData(uranus, 'uranus.txt')
ephemeris_n = neptune.getData(neptune, 'neptune.txt')
ephemeris_p = pluto.getData(pluto, 'pluto.txt')

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
    ax.set_zbound(-minmax/10, minmax/10)

    ax.scatter3D(0,0,0,zdir='z')
    ax.scatter3D(ephemeris_m1[num][0], ephemeris_m1[num][1], ephemeris_m1[num][2])
    ax.scatter3D(ephemeris_v[num][0], ephemeris_v[num][1], ephemeris_v[num][2])
    ax.scatter3D(ephemeris_e[num][0], ephemeris_e[num][1], ephemeris_e[num][2])  
    ax.scatter3D(ephemeris_m[num][0], ephemeris_m[num][1], ephemeris_m[num][2])
    ax.scatter3D(ephemeris_j[num][0], ephemeris_j[num][1], ephemeris_j[num][2])
    ax.scatter3D(ephemeris_s[num][0], ephemeris_s[num][1], ephemeris_s[num][2])
    ax.scatter3D(ephemeris_u[num][0], ephemeris_u[num][1], ephemeris_u[num][2])
    ax.scatter3D(ephemeris_n[num][0], ephemeris_n[num][1], ephemeris_n[num][2])
    ax.scatter3D(ephemeris_p[num][0], ephemeris_p[num][1], ephemeris_p[num][2])

anim = animation.FuncAnimation(fig, func, 4750, interval=1, blit=False)


plt.show()