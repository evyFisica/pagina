 
#!/usr/bin/env python
 
# import useful modules
import matplotlib 
from numpy import *
from pylab import *
 
# use LaTeX, choose nice some looking fonts and tweak some settings
matplotlib.rc('font', family='serif')
matplotlib.rc('font', size=16)
matplotlib.rc('legend', fontsize=16)
matplotlib.rc('legend', numpoints=1)
matplotlib.rc('legend', handlelength=1.5)
matplotlib.rc('legend', frameon=False)
matplotlib.rc('xtick.major', pad=7)
matplotlib.rc('xtick.minor', pad=7)
matplotlib.rc('text', usetex=True)
matplotlib.rc('text.latex', 
              preamble=[r'\usepackage[T1]{fontenc}',
                        r'\usepackage{amsmath}',
                        r'\usepackage{txfonts}',
                        r'\usepackage{textcomp}'])
 
close('all')
#figure(figsize=(6, 4.5))
 
# generate grid
x=linspace(-1, 1, 20)
y=linspace(-1, 1, 20)
x, y=meshgrid(x, y)
      
def F(x,y):
  return x, -y
 
# calculate vector field
Fx, Fy=F(x, y)
# plot vecor field
quiver(x, y, Fx, Fy, pivot='middle', headwidth=4, headlength=6)
xlabel('$x$')
ylabel('$y$')
axis('image')
savefig('exemplo2.png')
show()