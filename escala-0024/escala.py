'''
Abre todos los .txt y crea el .csv con los pares de puntos (Vin, Vout) donde 
Vin es el voltaje de referencia y Vout es el voltaje que medimos.
'''

#%%

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime


v_in = [1,2,5,8,-1,-2,-5,-8,0]
v_in = [i*1000 for i in v_in]

v_out = []; std_dev = [];
a = 100000
b = 200000

t0 = datetime.now()

for i in range(9):

    data = np.loadtxt('escala-8-oct/18o0800{}.txt'.format(i),skiprows=1)
    v_out.append(np.mean(data[a:b,1]))
    std_dev.append(np.std(data[a:b,1]))
    print(datetime.now()-t0)
    
    
#%%

plt.figure(12)    
plt.errorbar(v_in,v_out,yerr=std_dev,fmt='.')
plt.xlabel('Vin')
plt.ylabel('Vout')
plt.show()


#%% Guardo los puntos para hacer el reescaleo

import csv

with open('transf_escala.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(zip(v_in,v_out,std_dev))


#%% Ajusto la curva para hacer la transformación
    
from scipy import optimize

fitfunc = lambda p,x: p[0]*x+p[1]

p0 = [-2,2] 

# Distancia a la función objetivo
errfunc = lambda p,x,y: fitfunc(p,x)-y 

x = np.array(v_in)
y = np.array(v_out)

out = optimize.leastsq(errfunc, p0, args=(x,y), full_output=1)
p1 = out[0]
covar = out[1]

# Grafico para chequear el fitteo
plt.figure(34)
plt.plot(x, y, ".", x, fitfunc(p1, x), "-", linewidth=1)
plt.grid()
plt.xlabel('Vin')
plt.ylabel('Vout')
plt.show()

