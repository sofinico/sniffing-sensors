#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt

#%% 

# Cargo los datos de la escala y los ajusto por una lineal

data = np.loadtxt('escala-0024/escala.csv', delimiter = ',')

vin = data[:,0]
vout = data[:,1]

    
fitfunc = lambda p,x: p[0]*x+p[1]
p0 = [-2,2] 

# Distancia a la función objetivo
errfunc = lambda p,x,y: fitfunc(p,x)-y 

x = np.array(vout)
y = np.array(vin)

out = optimize.leastsq(errfunc, p0, args=(x,y), full_output=1)
p1 = out[0]
covar = out[1]

# Grafico para chequear el fitteo
plt.figure(34)
plt.plot(x, y, 'ro', x, fitfunc(p1, x), 'r-' , linewidth=1)
plt.xlabel('Vout (mV)')
plt.ylabel('Vin (mV)')
plt.tight_layout()
plt.show()

#%%

# Cargo los datos a reescalear

d = np.loadtxt('AWM2100/datos-sin-escala/lejos_exh_pos.txt', 
                  skiprows = 1)
t = d[:,0]
v = d[:,1]

#%% 

# Reescaleo los datos

vreal = fitfunc(p1,v)

plt.figure(100)
plt.plot(t,v,'k-')
plt.plot(t,vreal,'r-')
plt.xlabel('tiempo (s)')
plt.ylabel('voltaje (mV)')
plt.tight_layout()
plt.show()


#%% 

# Los guardo
    
f = open('AWM2100/dormido/lejos.txt', 'w')

print('t(ms) reescaleado(mV)', file=f)
for i in range(len(vreal)):
    print(str(t[i]) + ' ' + str(vreal[i]), file=f)
f.close()

del f, i


