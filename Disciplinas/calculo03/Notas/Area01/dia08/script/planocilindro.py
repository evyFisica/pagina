from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#x   = np.linspace(0, 2, 100)
#y   = np.linspace(0, 2, 100)
#x,y = np.meshgrid(x,y)
#z_grid = 2.0-x-y
#z_surface = z_grid


#Zm = np.ma.masked_where(z_grid < 0, (z_surface))
#z_surface[np.where(np.ma.getmask(Zm)==True)] = np.nan


phi = np.linspace(0, np.pi/2.0, 100)
r = np.ones(100)
h = np.linspace(0, 1, 100)



x1 = np.outer(np.cos(phi), r)
y1 = np.outer(np.sin(phi), r)
z1 = np.outer(2.0-np.cos(phi)-np.sin(phi), h)

#ax.plot_surface(x, y, z_surface,  rstride=1, cstride=1, linewidth=0.0, alpha=0.25, color="r")

ax.plot_surface(x1, y1, z1,  rstride=1, cstride=1, linewidth=0.0, alpha=0.50, color="b")#"#C3D9F1")



#ax.set_xticks([0.0, 0.25, 0.5, 0.75, 1.0])
#ax.set_yticks([0.0, 0.25, 0.5, 0.75, 1.0])
#ax.set_zticks([0.0, 0.25, 0.5, 0.75, 1.0])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


ax.set_xlim(0, 2.1)
ax.set_ylim(0, 2.1)
ax.set_zlim(0.0, 2.0)

ax.view_init(elev=25.0, azim=45.0)
plt.savefig("paracil.png")


#animacao
#for ii in xrange(0,360,36):
  #ax.view_init(elev=10., azim=ii)
  #plt.savefig("movie"+str(ii)+".png")

plt.show()



