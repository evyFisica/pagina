 
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy
from mpl_toolkits.mplot3d.axes3d import Axes3D
from  matplotlib import patches
from matplotlib.figure import Figure
from matplotlib import rcParams
import matplotlib.colors as colors

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1, 2, 1,projection='3d')

pole_positions_orig = [-0.6+0.73j];
zero_positions_orig = [0.29-0.41j];

surface_limit = 1.7;
min_val = -surface_limit;
max_val = surface_limit;

surface_resolution = 0.0333;

X = numpy.arange(min_val,max_val,surface_resolution)
Y = numpy.arange(min_val,max_val,surface_resolution)
X, Y = numpy.meshgrid(X, Y)

z_grid = X + Y*1j;
z_surface = z_grid*0;

pole_positions = numpy.round(pole_positions_orig,1) + surface_resolution/2+(surface_resolution/2)*1j;
zero_positions = numpy.round(zero_positions_orig,1) + surface_resolution/2 +(surface_resolution/2)*1j;

for k in range(0, len(zero_positions)):
    z_surface = z_surface + 20*log10((z_grid - zero_positions[k].real - zero_positions[k].imag*1j));
    z_surface = z_surface + 20*log10((z_grid - zero_positions[k].real + zero_positions[k].imag*1j));

for k in range(0, len(pole_positions)):
    z_surface = z_surface - 20*log10((z_grid - pole_positions[k].real - pole_positions[k].imag*1j));
    z_surface = z_surface - 20*log10((z_grid - pole_positions[k].real + pole_positions[k].imag*1j));    





#Zm = ma.masked_where((abs(z_grid) < 1.09) & (abs(z_grid) > 0.91), (z_surface))
#z_surface = Zm;


Zm = ma.masked_where((abs(z_grid) < 1.02) & (abs(z_grid) > 0.98), (z_surface))
z_surface[where(ma.getmask(Zm)==True)] = numpy.nan


colors2 = cm.jet;
colors2.set_bad('k');

cmap = cm.jet
lev = numpy.arange(-30,30,1);
norml = colors.BoundaryNorm(lev, 256)
surf = ax.plot_surface(X, Y,z_surface, rstride=1, cstride=1, cmap=colors2,linewidth=0, antialiased=True, norm = norml)



#surf = ax.plot_surface(X, Y,z_surface, rstride=2, cstride=2, cmap=colors2,linewidth=0, antialiased=False)


ticks = [-1, 1]; 
z_ticks = [-30,-20,-10,0,10,20,30]; 
ax.set_xticks(ticks);
ax.set_yticks(ticks);   
ax.set_zticks(z_ticks);

ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_zlabel('Mag(db)',ha='left')
plt.setp(ax.get_zticklabels(), fontsize=7)
plt.setp(ax.get_xticklabels(), fontsize=7)  
plt.setp(ax.get_yticklabels(), fontsize=7)


ax = fig.add_subplot(1, 2, 2,projection='3d')
surf = ax.plot_surface(X, Y,ma.getmask(z_surface), rstride=2, cstride=2, cmap=colors2,linewidth=0, antialiased=False)



ax.grid(b=None);
show();