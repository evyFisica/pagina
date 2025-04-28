from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

U = np.linspace(0, 2, 20)
V = np.linspace(0, np.pi, 180)

u, v = np.meshgrid(U, V)

x = u
y = np.sqrt(4-u**2)*np.cos(v)
z = np.sqrt(4-u**2)*np.sin(v)


ax.plot_surface(x, y, z, alpha=0.3, color='blue', linewidth=0, antialiased=False)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.savefig("teste.png")

plt.show()
