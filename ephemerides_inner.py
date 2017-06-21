# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:15:09 2017

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
        
mercury = planet
venus = planet
earth = planet
mars = planet

ephemeris_m1 = mercury.getData(mercury, 'mercury.txt')
ephemeris_v = venus.getData(venus, 'venus.txt')
ephemeris_e = earth.getData(earth, 'earth.txt')
ephemeris_m = mars.getData(mars, 'mars.txt')

minmax = 130000000

fig = plt.figure()
ax = p3.Axes3D(fig)

s=100

def func(num):
    ax.cla()
    
    ax.autoscale(False, axis='both')
    ax.autoscale(False, axis='z')

    ax.set_xbound(-minmax, minmax)
    ax.set_ybound(-minmax, minmax)
    ax.set_zbound(-minmax/10, minmax/10)

    ax.scatter3D(0,0,0,zdir='z', c='yellow', s=1000)
    ax.scatter3D(ephemeris_m1[num][0], ephemeris_m1[num][1], ephemeris_m1[num][2], c='grey', s=0.38*s)
    ax.scatter3D(ephemeris_v[num][0], ephemeris_v[num][1], ephemeris_v[num][2], c='orange', s=0.95*s)
    ax.scatter3D(ephemeris_e[num][0], ephemeris_e[num][1], ephemeris_e[num][2], c='blue', s=s)  
    ax.scatter3D(ephemeris_m[num][0], ephemeris_m[num][1], ephemeris_m[num][2], c='red', s=0.53*s)
    
anim = animation.FuncAnimation(fig, func, 4750, interval=1, blit=False)

plt.show()