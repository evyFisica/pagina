#!/usr/bin/env python
#-*- coding: utf-8 -*-

from numpy import *
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

tmax = 10.0
dt   = 5

fig = p.figure()
ax = fig.gca(projection='3d')
t = linspace(0, 2*np.pi, 100)
x = np.cos(t)
y = np.cos(t)
z = 2*np.cos(t/2.0)
ax.plot(x, y, z, label=r'$\mathbf{r}(t) = t \mathbf{i} + \frac{\sqrt{2}}{2}t^2\mathbf{j} + \frac{1}{3}t^3\mathbf{k}$')
x = t
y = t**2
z = t**3

ax.plot(x, y, z, label=r'$\mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} + t^3\mathbf{k}$')

ax.set_xlabel('X', size=15)
ax.set_ylabel('Y', size=15)
ax.set_zlabel('Z', size=15)

#ax.set_autoscale_on(False)
#ax.set_xlim3d(0,10, 2.5)
#ax.set_ylim3d(0,100, 25)
#ax.set_zlim3d(0,1000, 250)

#ax.set_xticks([0, 2.5, 5, 7.5, 10])
#ax.set_yticks([0, 25, 50, 75, 100])
#ax.set_zticks([0, 250, 500, 750, 1000])

ax.legend(loc='upper left')

p.savefig('fig.png')

p.show()
