from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-1.3, 1.3, 0.1)
xlen = len(X)
Y = np.arange(-1.3, 1.3, 0.1)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
Z = 1 - X**2

colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[x, y] = colortuple[(x + y) % len(colortuple)]

#surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=colors,
        #linewidth=0, antialiased=False)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=True)        

#surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
        #linewidth=0, antialiased=False, cmap=cm.jet)


ax.set_zlim3d(-1, 1)
ax.w_zaxis.set_major_locator(LinearLocator(6))

plt.show()

