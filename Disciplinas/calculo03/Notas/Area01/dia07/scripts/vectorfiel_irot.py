 
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
x=linspace(-50, 50, 20)
y=linspace(-50, 50, 20)
x, y=meshgrid(x, y)
 
def E(x, y):
    b = np.sqrt(x**2 + y**2)
    return x / b, -y/b
 
# calculate vector field
Ex, Ey=E(x, y)
# plot vecor field
quiver(x, y, Ex, Ey, pivot='middle', headwidth=4, headlength=6)
xlabel('$x$')
ylabel('$y$')
axis('image')

plt.title(u'$\mathbf{F} = \dfrac{x\,\mathbf{i} -y \,\mathbf{j}}{\sqrt{x^2+y^2}}$')
plt.tight_layout()

plt.axhline(0, color='yellow')
plt.axvline(0, color='yellow')

savefig('exemplo04.png')

show()