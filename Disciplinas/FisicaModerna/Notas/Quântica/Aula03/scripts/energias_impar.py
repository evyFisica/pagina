#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#Modulos python
import numpy as np
import scipy.interpolate
import matplotlib as mpl
import matplotlib.pyplot as plt
 
#*******************************************
x  = np.linspace(0,8.0*np.pi/2.0,700)

tol = 10

y1 = -1.0/np.tan(x)
y1[y1 > tol]  = np.nan
y1[y1 < -tol] = np.nan

x0 = 11.0*np.pi/3.0
y2 = np.sqrt((x0/x)**2 - 1.0)
y2[y2 > tol]  = np.nan
y2[y2 < -tol] = np.nan

x0 = 8.0*np.pi/3.0
y3 = np.sqrt((x0/x)**2 - 1.0)
y3[y3 > tol]  = np.nan
y3[y3 < -tol] = np.nan

x0 = 5.0*np.pi/3.0
y4 = np.sqrt((x0/x)**2 - 1.0)
y4[y4 > tol]  = np.nan
y4[y4 < -tol] = np.nan

x0 = 2.0*np.pi/3.0
y5 = np.sqrt((x0/x)**2 - 1.0)
y5[y5 > tol]  = np.nan
y5[y5 < -tol] = np.nan

plt.axhline(0, color='black')
 
#plotando os dados
plt.plot(x, y1, linestyle='-', color='red', linewidth=2, label=r"$-\cot \theta$")
plt.plot(x, y2, linestyle='-', color='blue', linewidth=2, label=r"$\theta_0 = 11\pi/3$")
plt.plot(x, y3, linestyle='-', color='green', linewidth=2, label=r"$\theta_0 = 8\pi/3$")
plt.plot(x, y4, linestyle='-', color='magenta', linewidth=2, label=r"$\theta_0 = 5\pi/3$")
plt.plot(x, y5, linestyle='-', color='cyan', linewidth=2, label=r"$\theta_0 = 2\pi/3$")
 
#plt.legend(loc=(0.75,0.8))
plt.legend(loc=0)
 
plt.grid(True)
 
plt.xlabel(r'$\theta$', fontsize=20)
 
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=20)
 
plt.ylabel(r'$g(\theta),$  $f(\theta)$', fontsize=20)

#plt.xticks([0, np.pi/2., np.pi, 3*np.pi/2., 2*np.pi, 5*np.pi/2.0, 3*np.pi, 7*np.pi/2.0, 4*np.pi],
           #['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$', r'$\frac{7\pi}{2}$', r'$4\pi$'])
 
#plt.title("Exemplo", fontsize=30)
 
plt.tight_layout()
#plt.savefig('energias_impar.png')
 
plt.show()