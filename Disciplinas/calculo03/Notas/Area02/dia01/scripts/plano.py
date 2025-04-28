from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

def clip_z_data(z):
  return z if 0.0 <= z <= 3.0 else n.nan

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0.0, 1.0, 0.01)
Y = np.arange(0, 2.0, 0.01)
X, Y = np.meshgrid(X, Y)
Z = 3.0*(1.0 - X - Y / 2.0)
#Z = clip_z_data(Z)
Z = np.where(Z >= 0, Z, np.nan)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=True)
#ax.set_zlim(-20, 20)

#ax.set_xticks([0, np.pi/2, np.pi],
           #['$0$', r'$\frac{\pi}{2}$', r'$\pi$'])

ax.xaxis.set_major_locator(LinearLocator(0))
ax.yaxis.set_major_locator(LinearLocator(0))
ax.zaxis.set_major_locator(LinearLocator(0))

#ax.set_zlim3d(0.0,3.0)

#ax.zaxis.set_major_locator(LinearLocator(5))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f'))

ax.set_xlabel('x', fontsize=20)
ax.set_ylabel('y', fontsize=20)
ax.set_zlabel('z', fontsize=20)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
