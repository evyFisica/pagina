from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(1, 4, 100)
v = np.linspace(0, 2*np.pi, 100)

z = np.outer(u,np.ones(np.size(u)))
x = np.outer(u,np.cos(v))
y = np.outer(u,np.sin(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("exemplo13.png")

plt.show()