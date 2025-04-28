from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 1, 100)
v = np.linspace(0, 1, 100)

x = np.outer(np.sqrt(2.0)*u,np.ones(np.size(v)))
y = np.outer(np.sqrt(2.0)*u,np.ones(np.size(v)))
z = np.outer(np.ones(np.size(u)),5*v)
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='#ffff99')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x = np.outer(u,np.ones(np.size(v)))
y = np.outer(np.sqrt(3.0)*u,np.ones(np.size(v)))
z = np.outer(np.ones(np.size(u)),5*v)
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='#ffff99')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

u = np.linspace(np.pi/6, np.pi/4, 100)
v = np.linspace(0, 1, 100)

x = np.outer(2*np.sin(u),np.ones(np.size(v)))
y = np.outer(2*np.cos(u),np.ones(np.size(v)))
z = np.outer(np.ones(np.size(u)),5*v)
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("plano2.png")

plt.show()