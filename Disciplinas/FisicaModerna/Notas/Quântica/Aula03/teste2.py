import matplotlib.pyplot as plt
import numpy as np
#from sympy import *
import sympy as sy

x,L,n=sy.symbols('x,L,n')

P = (sy.sqrt(2/L) *sy.sin(n*sy.pi*x/L))**2

f =  sy.simplify(sy.Integral(x*P,(x,L/4,3*L/4)).doit())
g1 = f.subs(L, 10)

sy.pprint(g1)
f1 = sy.plot(g1,(n,0,10),ylabel=r'$\psi ^2(x)$', show=False)

#x, y = symbols("x y")
#hp = plot_implicit(Eq(x**2 + y**2, 4), (x, -3, 3), (y, -3, 3))
#fig = hp._backend.fig
fig = f1._backend.fig

ax = hp._backend.ax
#xx = yy = np.linspace(-3,3)
#ax.plot(xx,yy) # y = x
#ax.plot([0],[0],'o') # Point (0,0)
#ax.set_aspect('equal','datalim')
fig.canvas.draw()
