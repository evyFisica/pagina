#!/usr/bin/env python
# -*- coding: utf-8 -*-

#https://stackoverflow.com/questions/46810880/display-two-sympy-plots-as-two-matplotlib-subplots

import numpy as np
import sympy as sy
from scipy.linalg import eigh
import matplotlib.pyplot as plt

#*******************************************



def move_sympyplot_to_axes(p, ax):
    backend = p.backend(p)
    backend.ax = ax
    backend._process_series(backend.parent._series, ax, backend.parent)
    backend.ax.spines['right'].set_color('none')
    backend.ax.spines['bottom'].set_position('zero')
    backend.ax.spines['top'].set_color('none')
    plt.close(backend.fig)

#*******************************************



x,L,n=sy.symbols('x,L,n')

P = (sy.sqrt(2/L) *sy.sin(n*sy.pi*x/L))**2

f =  sy.simplify(sy.Integral(x*P,(x,L/4,3*L/4)).doit())

#

#f = sy.Lambda(x, x**2)
p = []
for i in range(1,4,1):
  g1 = P.subs(L, 10)
  g  = g1.subs(n, i)
  sy.pprint(g)
  f1 = sy.plot(g,(x,0,10), show=False)
  p.append(f1)
#,ylabel=r'$\psi ^2(x)$',
fp = p[0]
fp.extend(p[1]) #ou este metodo
fp.append(p[2][0]) #ou este outro



fig, (ax) = plt.subplots(ncols=1)
move_sympyplot_to_axes(fp, ax)

plt.show()
