from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(-3, 3, 100)
v = np.linspace(-1, 1, 100)

x = -1 + np.outer((u+1),v)
y = 1 + np.outer((0.25*u**2),v)
z = 1 + np.outer(np.ones(np.size(u)),v)
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("exemplo07.png")

plt.show()