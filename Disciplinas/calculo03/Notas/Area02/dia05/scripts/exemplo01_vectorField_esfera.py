#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt
#import numpy as np

#fig = plt.figure()
#ax = fig.gca(projection='3d')

#x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      #np.arange(-0.8, 1, 0.2),
                      #np.arange(-0.8, 1, 0.8))

#u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
#v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
#w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     #np.sin(np.pi * z))

#ax.quiver(x, y, z, u, v, w, length=0.1)

#plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()

v = np.linspace(0, 2 * np.pi/2.0, 100)
u = np.linspace(0, 1, 100)

x = np.outer(np.sin(v),np.cos(v))
y = np.outer(np.sin(v),np.sin(v))
z = np.outer(np.cos(v),np.ones(np.size(u)))


ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#plt.savefig("cilCortado.png")

#ax1.set_ylim([-5, 5])
#ax1.set_xlim([-5, 5])

#plt.savefig("cilindrocortado.png")

plt.show()