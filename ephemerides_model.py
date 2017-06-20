# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 17:29:08 2017

@author: jaywe
"""

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

fig = plt.figure()
ax = p3.Axes3D(fig)

extra = 1

data = np.empty([10, 3])
for i in range(1, 10):
    for j in range(1, 3):
        data[i][j] = np.random.randint(0, 10)
        
print(data)

ax.scatter(0,0,0,zdir='z')

def func(num):
    #ax.cla()
    ax.scatter(0,0,0,zdir='z')
    ax.scatter(data[num][0], data[num][1], data[num][2])
    
        
#==============================================================================
#     ax.scatter(10,10,10)
#     ax.scatter(num, num, num)
#     ax.scatter(-num, -num, -num)
#==============================================================================

    
    

anim = animation.FuncAnimation(fig, func, 10, interval=1000, blit=False)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('test')



plt.show()