from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()

rciclo = 3.0
rcirc  = 1.0
passo  = 10.0/(2.0*np.pi)

u = np.linspace(0, 6 * np.pi, 600)
v = np.linspace(0, 2 * np.pi, 100)

nor = 1.0 / np.sqrt(rciclo**2 + passo**2)

Nsx = -rciclo*nor*np.cos(u)
Nsy = -rciclo*nor*np.sin(u)
Nsz = np.zeros(np.size(u))

Bsx = rciclo*passo*nor**2*np.sin(u)
Bsy = -rciclo*passo*nor**2*np.cos(u)
Bsz = rciclo**2*nor**2*np.ones(np.size(u))

xts = rciclo*np.cos(u)
yts = rciclo*np.sin(u)
zts = passo* u

#CIRCUNFERENCIA AO LONGO DA TRAJETORIA
xc = np.outer(Nsx,np.cos(v)) + np.outer(Bsx,np.sin(v))
yc = np.outer(Nsy,np.cos(v)) + np.outer(Bsy,np.sin(v))
zc = np.outer(Nsz,np.cos(v)) + np.outer(Bsz,np.sin(v))

#TRAJETORIA
x = np.outer(xts, np.ones(np.size(v))) + xc
y = np.outer(yts, np.ones(np.size(v))) + yc
z = np.outer(zts, np.ones(np.size(v))) + zc

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,  rstride=4, cstride=4, cmap=cm.coolwarm, antialiased=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#plt.savefig("lissa01.png")

plt.show()