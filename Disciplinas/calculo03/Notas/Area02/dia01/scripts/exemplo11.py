from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(-2, 2, 100)
v = np.linspace(0, 1, 100)

x = np.outer(u,np.ones(np.size(v)))
y = np.outer(u**2,np.ones(np.size(v)))
z = np.outer(np.ones(np.size(u)),8*v)
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("exemplo11.png")

plt.show()