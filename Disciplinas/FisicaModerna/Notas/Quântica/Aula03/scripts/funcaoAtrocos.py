 
#/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams['text.latex.unicode'] = True
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = '\usepackage{amsthm}', '\usepackage{amsmath}', '\usepackage{amssymb}',
'\usepackage{amsfonts}', '\usepackage[T1]{fontenc}', '\usepackage[utf8]{inputenc}, \usepackage{multicol}'
rcParams['legend.handleheight'] = 3.0
#This fixes the legend line be placed at same height that text legend


def f(x):
    return np.piecewise(x, [x < 2.0, x > 2.0], [lambda x: x ** 2.0, lambda x: 4.0])


fig, ax = plt.subplots()
x = np.linspace(-5.0, 5.0, 1000)
ax.axis([x[0], x[-1], x[0], x[-1]])
ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')
ax.spines['left']
ax.spines['bottom']
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ticks = []
for i in range(int(x[0]), int(x[-1] + 1), 1):
    ticks.append(i)
ticks.remove(0)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.plot(x, f(x), 'b-', 2, 4, 'wo', markeredgecolor='b',
        markerfacecolor='w', lw=2.0)
tlegend = r'$f(x)=\left\{\begin{array}{lr} x^2 & : x<2\\ 4 & : x>2\end{array}\right\}$'
ax.legend([tlegend], loc='lower right')
ax.set_title(ur'$Funcion\; A\; Trozos$') # If you use accents put ur option.
ax.grid('on')
plt.show()