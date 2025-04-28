import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(0, 7/2 * np.pi, 200)
y = (np.sin(theta))**3
x = (np.cos(theta))**3
z = theta
ax.plot(x, y, z)
fig.savefig('exemplo04.png')
plt.show()
