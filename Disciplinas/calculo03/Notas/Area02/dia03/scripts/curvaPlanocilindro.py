from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()

v = np.linspace(0, 2 * np.pi, 100)
u = np.linspace(0, 1, 100)

x = np.outer(np.ones(np.size(u)),2.0*np.cos(v))
y = np.outer(np.ones(np.size(u)),2.0*np.sin(v))
z = np.outer(np.ones(np.size(u)),8.0-2.0*np.sin(v))


ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.savefig("cone01.png")

#ax1.set_ylim([-5, 5])
#ax1.set_xlim([-5, 5])
#ax.set_zlim([0, 10])

#plt.savefig("cilindrocortado.png")

plt.show()