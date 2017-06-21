# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:19:10 2017

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

jupiter = planet
saturn = planet
uranus = planet
neptune = planet
pluto = planet

ephemeris_j = jupiter.getData(jupiter, 'jupiter.txt')
ephemeris_s = saturn.getData(saturn, 'saturn.txt')
ephemeris_u = uranus.getData(uranus, 'uranus.txt')
ephemeris_n = neptune.getData(neptune, 'neptune.txt')
ephemeris_p = pluto.getData(pluto, 'pluto.txt')

minmax = 2000000000

fig = plt.figure()
ax = p3.Axes3D(fig)

s=3

def func(num):
    ax.cla()
    
    ax.autoscale(False, axis='both')
    ax.autoscale(False, axis='z')

    ax.set_xbound(-minmax, minmax)
    ax.set_ybound(-minmax, minmax)
    ax.set_zbound(-minmax/10, minmax/10)

    ax.scatter3D(0,0,0,zdir='z', c='yellow', s=1000)
    ax.scatter3D(ephemeris_j[num][0], ephemeris_j[num][1], ephemeris_j[num][2], c='sandybrown', s=112*s)
    ax.scatter3D(ephemeris_s[num][0], ephemeris_s[num][1], ephemeris_s[num][2], c='bisque', s=95*s)
    ax.scatter3D(ephemeris_u[num][0], ephemeris_u[num][1], ephemeris_u[num][2], c='darkturquoise', s=40*s)
    ax.scatter3D(ephemeris_n[num][0], ephemeris_n[num][1], ephemeris_n[num][2], c='deepskyblue', s=39*s)
    ax.scatter3D(ephemeris_p[num][0], ephemeris_p[num][1], ephemeris_p[num][2], c='dimgray', s=s)

anim = animation.FuncAnimation(fig, func, 4750, interval=1, blit=False)

plt.show()