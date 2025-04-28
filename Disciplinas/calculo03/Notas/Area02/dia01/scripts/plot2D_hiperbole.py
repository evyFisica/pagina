 
##!/usr/bin/env python
 
##Modulos python
#import numpy as np
#import scipy.interpolate
#import matplotlib as mpl
#import matplotlib.pyplot as plt
 
##*******************************************
 
##le os dados e armazena em 2 vetores: x, y.
#t = np.linspace(-1, 1, 100)
#x = 3 * np.cosh(t)
#y = 5 * np.sinh(t)

##x, y = np.loadtxt('dados01.dat', unpack=True)
 
##plotando os dados
#plt.plot(x, y, '-')
#plt.show()

from sympy import var, Plot
var('x y')
Plot((x/3)**2 - (y/5)**2=1)