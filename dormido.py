# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:11:52 2018

@author: noelp
"""

import numpy as np
from matplotlib import pyplot as plt


#%% 
'''SIMIL CANULA'''

directorio = 'C:/Users/noelp/Documents/Facultad/Exactas/Laboratorio/LABO 6-7/Poster/sniffing-sensors-data/'
nf = '24PC/dormido/470ohm_similcanula.txt'
data = np.loadtxt(directorio+nf,skiprows=1)

#%% RAW

t = data[:,0]/1000

def applyPlotStyle():
    plt.xlabel('Tiempo (s)',fontsize=15)
    plt.ylabel('Voltaje (V)',fontsize=15)
#    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)

    
offset = 5
ventana = 2.5
    
plt.figure(4703, frameon=False)
plt.plot(t-offset, post, linewidth='1.5',color = 'k')
plt.axhline(y=1.695,xmin=0.32,xmax=0.5, color='lightgrey', linewidth='5')
plt.text(0.6,1.689,'0.6 seg', fontsize=12)
plt.axvline(x=0.25,ymin=0.15,ymax=0.3,color='lightgrey',linewidth='5')
plt.text(0.5,1.65,'10mV', fontsize=12, rotation=90)
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([1.63,1.7])
applyPlotStyle()
plt.axis('off')
plt.tight_layout()
plt.show()

#%%

''' 2100 Despierto'''

nam = 'despierto2100.txt'
d24 = np.loadtxt(directorio+nam,skiprows=1)

man = 'desperto2100_inh.txt'
d24_inh = np.loadtxt(directorio+man,skiprows=1)

#%%
t24 = d24[:,0]; v24 = d24[:,1]
ix = d24_inh[:,0]; iy = d24_inh[:,1]; fx = d24_inh[:,2]; fy = d24_inh[:,3]; px = d24_inh[:,4]; py = d24_inh[:,5]
#%%

def applyPlotStyle():
    plt.xlabel('Tiempo (s)',fontsize=15)
    plt.ylabel('Voltaje (V)',fontsize=15)
#    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)


offset = 245
ventana = 2
   
plt.figure(472, frameon=False)
plt.axhline(y=-0.008,xmin=0.25,xmax=0.5, color='lightgrey', linewidth='5')
plt.text(0.5,-0.0088,'0.5 seg', fontsize=12)
plt.axvline(x=0.25,ymin=0.12,ymax=0.22,color='lightgrey',linewidth='5')
plt.text(0.55,-0.0065,'4mV', fontsize=12, rotation=90)
plt.plot(t24-offset, v24, linewidth='1.5',color = 'k')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([-0.01,0.0065])
plt.plot(ix-offset, iy,'kx')
plt.axis('off')
applyPlotStyle()
plt.tight_layout()
plt.show()

#%%
'''3100 Despierto'''

nam = 'despierto3100.txt'
d31 = np.loadtxt(directorio+nam,skiprows=1)

man3 = 'desperto3100_inh.txt'
d31_inh = np.loadtxt(directorio+man3,skiprows=1)

#%%
t31 = d31[:,0]; v31 = d31[:,1]
ix31 = d31_inh[:,0]; iy31 = d31_inh[:,1]; fx31 = d31_inh[:,2]; fy31 = d31_inh[:,3]; px31 = d31_inh[:,4]; py31 = d31_inh[:,5]
#%%

def applyPlotStyle():
    plt.xlabel('Tiempo (s)',fontsize=15)
    plt.ylabel('Voltaje (V)',fontsize=15)
#    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)


offset = 7
ventana = 1.5
   
plt.figure(482, frameon=False)
plt.axhline(y=0.58,xmin=0.25,xmax=0.5, color='lightgrey', linewidth='5')
plt.text(0.5,0.6,'0.5 seg', fontsize=12)
plt.axvline(x=0.25,ymin=0.77,ymax=0.9,color='lightgrey',linewidth='5')
plt.text(0.35,0.45,'2mV', fontsize=12, rotation=90)
plt.plot(t31-offset, v31, linewidth='1.5',color = 'k')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([-0.1,0.68])
plt.plot(ix31-offset, iy31,'kx')
plt.axis('off')
applyPlotStyle()
plt.tight_layout()
plt.show()
