from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()

v = np.linspace(0, 2 * np.pi, 100)
u = np.linspace(1, 4, 100)

z = np.outer(u,np.cos(v))
y = np.outer(u,np.sin(v))
x = np.outer(u,np.ones(np.size(v)))


#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#plt.savefig("cone01.png")

#somente projeta a terceira coordenada, por isso coloque o X nesse ponto
ax1 = plt.subplot(111)
ax1.spines['left'].set_position('center')
#ax1.spines['right'].set_color('none')
ax1.spines['bottom'].set_position('center')
#ax1.spines['top'].set_color('none')
#ax1.spines['left'].set_smart_bounds(True)
#ax1.spines['bottom'].set_smart_bounds(True)
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

plt.contourf(z, y, x, colors='#C4F5FF')
x = np.cos(v)
y = np.sin(v)
ax1.plot(x,y, color="black")
x = 4.0*np.cos(v)
y = 4.0*np.sin(v)
plt.plot(x,y, color="black")

ax1.set_ylim([-5, 5])
ax1.set_xlim([-5, 5])

plt.savefig("cone02.png")

plt.show()