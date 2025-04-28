from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

phi = np.linspace(0, np.pi/2.0, 100)
r = np.ones(100)
h = np.linspace(0, 1, 100)


x = np.outer(np.cos(phi), r)
z = np.outer(np.cos(phi)**2, r)
y = np.outer(np.ones(np.size(r)), h)


x1 = np.outer(np.cos(phi), r)
y1 = np.outer(np.sin(phi), r)
z1 = np.outer(2.0-np.cos(phi)**2-2*np.sin(phi)**2, h)


x2 = np.outer(np.cos(phi), r)
y2 = np.outer(np.sin(phi), r)
z2 = np.outer(2.0-np.cos(phi)**2-2*np.sin(phi)**2, np.ones(np.size(r)))

ax.plot_surface(x, y, z,  rstride=9, cstride=10, linewidth=0.0, alpha=0.2, color="r")

ax.plot_surface(x1, y1, z1,  rstride=9, cstride=10, linewidth=0.0, alpha=0.2, color="b")

ax.plot_surface(x2, y2, z2,  rstride=9, cstride=10, linewidth=1.0, alpha=1, color="b")

ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0])
ax.set_zticks([0.0, 0.25, 0.5, 0.75, 1.0])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.view_init(elev=10.0, azim=35.0)
plt.savefig("paracil.png")

#animacao
#for ii in xrange(0,360,36):
  #ax.view_init(elev=10., azim=ii)
  #plt.savefig("movie"+str(ii)+".png")

plt.show()



