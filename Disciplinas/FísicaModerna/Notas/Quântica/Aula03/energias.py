#!/usr/bin/env python
 
from numpy import *

def constante_par(x,x0):
  k2 = x
  k1 = x * sqrt((x0/x)**2-1.)
  cp = exp(k1)*cos(k2)
  c  = sqrt(2.0/(1.0 + sin(2.0*k2)/(2.0*k2) + 2.*(cp**2*exp(-2.*k1)/(2.*k1)) ) )
  #print "\n", k1, k2, cp, exp(-2.*k1)
  return [c, cp, c*cp]

def constante_impar(x,x0):
  k2 = x
  k1 = x * sqrt((x0/x)**2-1.)
  cp = exp(k1)*sin(k2)
  c  = sqrt(2.0/(1.0 - sin(2.0*k2)/(2.0*k2) + 2.*(cp**2*exp(-2.*k1)/(2.*k1)) ) )
  #print "\n", k1, k2, cp, exp(-2.*k1)
  return [c, cp, c*cp]

toly = 5.0e-5
tolx = 0.2
x0  = input("theta_0 = ")

E = []

dx = x0 / 1000000.0
x  = 0
xs = 0
while True:
  x  = x + dx
  if (x > x0):
    break
  y1 = sqrt((x0/x)**2 - 1.0)
  y2 = tan(x)
  if (abs(y2-y1) <= toly and (x-xs) > tolx):
    xs = x
    print "Energia de estado simetrico em theta =", x, constante_par(x,x0)
    E.append(x)
  y3 = -1.0 / tan(x)  
  if (abs(y3-y1) <= toly and (x-xs) > tolx):
    xs = x
    print "Energia de estado antssimetrico em theta = ", x, constante_impar(x,x0)
    E.append(x)
    
#print "Constante C para o estado si
print E