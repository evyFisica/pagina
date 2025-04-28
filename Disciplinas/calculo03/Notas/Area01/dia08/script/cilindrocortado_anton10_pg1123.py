from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 1, 100)

x = np.outer(np.ones(np.size(v)),np.cos(u))
y = np.outer(np.ones(np.size(v)),np.sin(u))
z = np.outer(v,1-(np.sin(u))**2)
print z
ax.plot_surface(x, y, z,  rstride=6, cstride=6, color='b')
ax.set_xticks([-2.0, -1.0, 0.0, 1.0, 2.0])
ax.set_yticks([-2.0, -1.0, 0.0, 1.0, 2.0])
ax.set_zticks([0.0, 0.5, 1.0])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=20.0, azim=50.0)
plt.savefig("elipse2.png")

#animacao
#for ii in xrange(0,360,36):
  #ax.view_init(elev=10., azim=ii)
  #plt.savefig("movie"+str(ii)+".png")

plt.show()