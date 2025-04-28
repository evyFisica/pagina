from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 1, 100)

x = np.outer(v,1.5+np.cos(u))
y = np.outer(v,1.5+np.sin(u))
z = np.outer(2*v,np.ones(np.size(u)))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')

x = 1.5+np.outer(v,np.cos(u))
y = 1.5+np.outer(v,np.sin(u))
z = np.outer(2,np.ones(np.size(u)))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='w')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#plt.savefig("exemplo14.png")

plt.show() 
