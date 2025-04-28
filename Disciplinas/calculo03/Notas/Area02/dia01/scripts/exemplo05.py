from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 1, 100)

x = np.outer(2*np.sin(u),v)
y = np.outer(2*np.cos(u),v)
z = np.outer(np.ones(np.size(u)),-2*v)
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("exemplo05.png")

plt.show()