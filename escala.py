# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 18:57:48 2018

@author: noelp
"""


import numpy as np
from scipy import optimize

# Cargo los datos de la escala y los ajusto por una lineal

scaling = np.loadtxt('C:/Users/noelp/Documents/Git/sniffing-sensors/escala-0024/escala.csv', delimiter = ',')

vin = scaling[:,0]
vout = scaling[:,1]

    
fitfunc = lambda p,x: p[0]*x+p[1]
p0 = [-2,2] 

# Distancia a la función objetivo
errfunc = lambda p,x,y: fitfunc(p,x)-y 

x = np.array(vout)
y = np.array(vin)

out = optimize.leastsq(errfunc, p0, args=(x,y), full_output=1)
p1 = out[0]
covar = out[1]

del scaling; del vin; del vout; del p0; del errfunc; del x; del y
del out; del covar
