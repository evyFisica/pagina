from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, np.pi, 100)
v = np.linspace(0, 2*np.pi, 100)

x = np.outer(np.sin(u),np.cos(v))
y = np.outer(np.sin(u),np.sin(v))
z = np.outer(u,np.ones(np.size(u)))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("exemplo14.png")

plt.show()
