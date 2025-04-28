from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(-20, 20, 100)
v = np.linspace(0, 2*np.pi, 100)

y = np.outer(u,np.ones(np.size(u)))
x = np.outer(3*np.sqrt(1+(u/5)**2),np.cos(v))
z = np.outer(3*np.sqrt(1+(u/5)**2),np.sin(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("exemplo14.png")

plt.show()