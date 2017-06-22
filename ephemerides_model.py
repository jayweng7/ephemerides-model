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
#==============================================================================
#     strings from the horizon document that 
#     indicate the start and end of ephemeris data
#==============================================================================
    start = '$$SOE'
    end = '$$EOE'
    
    def __init__(self, name):
        self.name = name
        
#==============================================================================
#     function to read the data from horizons .txt file    
#==============================================================================
    
    def getData(self, filename):
        file = open(filename)
        s = file.readline()
        while (self.start not in s):        #Skip all lines until ephemeris data is reached
            s = file.readline()
            
        ephemeris = np.empty([4750, 3])     #4750 is enough for 13 years at 1 day step... 
        i = 0                               #TODO: make the array dynamic
        
        while True:
            s = file.readline()
            if (self.end in s):             #Go through each line until the end is reached
                break
            s1,s2,s3,s4,s5 = s.split(", ")  #Split the line at the commas: s1, s2 are dates, s3, s4, s5 are x, y, z positions
            s5 = re.sub(',', '', s5)        #Make s5 an integer basically
            ephemeris[i][0] = s3
            ephemeris[i][1] = s4
            ephemeris[i][2] = s5
            i += 1
        
        return ephemeris
        
planets = []                                #Consider putting the below into a list and iterating through for the .scatter() function

mercury = planet
venus = planet
earth = planet
mars = planet
jupiter = planet
saturn = planet
uranus = planet
neptune = planet
pluto = planet

ephemeris_m1 = mercury.getData(mercury, 'mercury.txt')      #Could also iterate this
ephemeris_v = venus.getData(venus, 'venus.txt')
ephemeris_e = earth.getData(earth, 'earth.txt')
ephemeris_m = mars.getData(mars, 'mars.txt')
ephemeris_j = jupiter.getData(jupiter, 'jupiter.txt')
ephemeris_s = saturn.getData(saturn, 'saturn.txt')
ephemeris_u = uranus.getData(uranus, 'uranus.txt')
ephemeris_n = neptune.getData(neptune, 'neptune.txt')
ephemeris_p = pluto.getData(pluto, 'pluto.txt')

minmax = 1850000000                                         #Axis bounds

fig = plt.figure()
ax = p3.Axes3D(fig)

s=10                                                        #Smallest size of planet

def func(num):
    ax.cla()
    
    ax.autoscale(False, axis='both')
    ax.autoscale(False, axis='z')

    ax.set_xbound(-minmax, minmax)
    ax.set_ybound(-minmax, minmax)
    ax.set_zbound(-minmax/10, minmax/10)
    
    #How to go about setting individual colours and sizes if iterating through a list? ......TODO

    ax.scatter3D(0,0,0,zdir='z', c='yellow')
    ax.scatter3D(ephemeris_m1[num][0], ephemeris_m1[num][1], ephemeris_m1[num][2], c='grey', s=s)
    ax.scatter3D(ephemeris_v[num][0], ephemeris_v[num][1], ephemeris_v[num][2], c='orange', s=s)
    ax.scatter3D(ephemeris_e[num][0], ephemeris_e[num][1], ephemeris_e[num][2], c='blue', s=s)  
    ax.scatter3D(ephemeris_m[num][0], ephemeris_m[num][1], ephemeris_m[num][2], c='red', s=s)
    ax.scatter3D(ephemeris_j[num][0], ephemeris_j[num][1], ephemeris_j[num][2], c='sandybrown', s=112*s)        #Gas giants are actually to
    ax.scatter3D(ephemeris_s[num][0], ephemeris_s[num][1], ephemeris_s[num][2], c='bisque', s=95*s)             #scale relative to Earth :)
    ax.scatter3D(ephemeris_u[num][0], ephemeris_u[num][1], ephemeris_u[num][2], c='darkturquoise', s=40*s)
    ax.scatter3D(ephemeris_n[num][0], ephemeris_n[num][1], ephemeris_n[num][2], c='deepskyblue', s=39*s)
    ax.scatter3D(ephemeris_p[num][0], ephemeris_p[num][1], ephemeris_p[num][2], c='dimgray', s=s)

anim = animation.FuncAnimation(fig, func, 4750, interval=1, blit=False)                                         #Animate the graph. 4750 frames, interval 1 ms

plt.show()