import matplotlib.pyplot as plt
import numpy as np
import sympy as sy


x,L,n=sy.symbols('x,L,n')

P = (sy.sqrt(2/L) *sy.sin(n*sy.pi*x/L))**2

f =  sy.simplify(sy.Integral(x*P,(x,0,L/3)).doit())
sy.pprint(f)

##Impime funções de probabilidade
#vx = np.arange(0,10,0.1)
#vy = np.zeros((vx.size))
#mg = []
#for i in range(1,5,1):
  #g1 = P.subs(L, 10)
  #g  = g1.subs(n, i)
  #sy.pprint(g)
  #gn = sy.lambdify(x, g, 'numpy')
  #vy = gn(vx)
  #plt.plot(vx, vy, '-', label=i)
  #plt.legend()
  
#plt.xlabel(r'$x$', fontsize=14)
#plt.ylabel(r'$P(x)$', rotation=0, fontsize=14, labelpad=20)
#plt.tight_layout()
#plt.savefig('fig17c.png')
#plt.show()


g = f.subs(L, 10)
#g  = g1.subs(x, 1)
gn = sy.lambdify(n, g, 'numpy')
vx = np.arange(0.01,10,0.1)
vy = gn(vx)
#ax = plt.subplot()
plt.plot(vx, vy, ':')


vx = np.arange(1,10,1)
vy = gn(vx)
plt.plot(vx, vy, marker="o", markersize=10, linestyle='')

plt.xlabel(r'$n$', fontsize=14)
plt.ylabel(r'$\left<\, x \,\right>$', rotation=0, fontsize=14, labelpad=20)
#ax.set_ylabel('abc', rotation=0, fontsize=20, labelpad=20) 
plt.tight_layout()

plt.savefig('fig17b.png')
plt.show()
