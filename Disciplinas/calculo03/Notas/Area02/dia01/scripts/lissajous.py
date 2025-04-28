from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()

v = np.linspace(0, 2 * np.pi, 100)
u = np.linspace(0, 10, 100)

z = np.outer(u,4.0*np.sin(v))
y = np.outer(u,4.0*np.sin(v/4.0))
x = np.outer(u,3.0*np.ones(np.size(v)))

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig("lissa01.png")

plt.show()