#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#Modulos python
import numpy as np
import scipy.interpolate
import matplotlib as mpl
import matplotlib.pyplot as plt


def f1p(L, C1, k1, x):
  return C1/np.sqrt(L)*np.exp(2.0*k1/L*x)

def f2p(L, C2, k2, x):
  return C2/np.sqrt(L)*np.cos(2.0*k2/L * x)

def f3p(L, C1, k1, x):
  return C1/np.sqrt(L)*np.exp(-2.0*k1/L*x)

def psi_p(L, C1, C2, k1, k2, x):
  return np.piecewise(x,[x<=-L/2., (x>-L/2.)&(x<L/2.)],
                           [lambda x: f1p(L, C1,k1,x),
                            lambda x: f2p(L, C2,k2,x), 
                            lambda x: f3p(L, C1,k1,x)])
#*******************************************

def f1i(L, C1, k1, x):
  return -C1/np.sqrt(L)*np.exp(2.0*k1/L*x)

def f2i(L, C2, k2, x):
  return C2/np.sqrt(L)*np.sin(2.0*k2/L * x)

def f3i(L, C1, k1, x):
  return C1/np.sqrt(L)*np.exp(-2.0*k1/L*x)

def psi_i(L, C1, C2, k1, k2, x):
  return np.piecewise(x,[x<=-L/2., (x>-L/2.)&(x<L/2.)],
                           [lambda x: f1i(L, C1,k1,x),
                            lambda x: f2i(L, C2,k2,x), 
                            lambda x: f3i(L, C1,k1,x)])
#*******************************************

L  = 2.0
x = np.linspace(-3.0,3.0,600)

fig, ax = plt.subplots()

#ax.axis([x[0], x[-1], x[0], x[-1]])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


ax.plot((-1.0, -1.0), (-1.0, 1.0), linestyle='--', color='cyan', linewidth=3)
ax.plot((1.0, 1.0), (-1.0, 1.0), linestyle='--', color='cyan', linewidth=3)

C1 = 17.9
C2 = 1.26
k1 = 3.80
k2 = 1.25
y = psi_p(L, C1, C2, k1, k2, x)

ax.plot(x, y, linestyle='-', label=r"$\psi_1$", linewidth=1)

C1 = 18.6
C2 = 1.23
k1 = 3.16
k2 = 2.45
y = psi_i(L, C1, C2, k1, k2, x)

ax.plot(x, y, linestyle='-', label=r"$\psi_2$", linewidth=1)

C1 = -5.8
C2 = 1.13
k1 = 1.74
k2 = 3.60
y = psi_p(L, C1, C2, k1, k2, x)

ax.plot(x, y, linestyle='-', label=r"$\psi_3$", linewidth=1)

plt.xticks([-2, -1, 0, 1, 2], ['$-L$', r'$-L/2$', r'$0$', r'$L/2$', r'$L$'])

ax.legend(loc=0)
 
plt.tight_layout()
plt.savefig("psi.png", format='png')
plt.show()
plt.close()
