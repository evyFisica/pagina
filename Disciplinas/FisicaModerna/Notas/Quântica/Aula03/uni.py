import numpy as np
from scipy.linalg import eigh
import matplotlib.pyplot as plt

W = 10 # width of well
n = 1000 # number of points
hbar = 1
m = 1
x = np.linspace(0, W, num=n+2)
h = x[1] - x[0] # step size

# Construction of the hamiltonian matrix
H = np.zeros([n, n])
for i in range(n):
    H[i, i] = -2
    if(i-1>=0):
        H[i, i-1] = 1
    if(i+1<n):
        H[i, i+1] = 1
H = -1*(hbar**2)/(2*m*(h**2))*H

# Solution
E, V = eigh(H, eigvals=(0, 10))

# Visualization
eigfun = np.zeros((n+2))
eigfun[1:-1] = V[:, 0]
plt.plot(x, np.abs(eigfun)**2)
eigfun[1:-1] = V[:, 1]
plt.plot(x, np.abs(eigfun)**2)
eigfun[1:-1] = V[:, 2]
plt.plot(x, np.abs(eigfun)**2)
plt.show()
