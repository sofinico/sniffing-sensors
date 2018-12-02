#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

#%% DIRECTO

nf = '24PC/dormido/47ohm_directo.txt'
data = np.loadtxt(nf,skiprows=1)

#%% RAW

t = data[:,0]/1000

pre = data[:,1]/1000
post = data[:,2]/1000

plt.figure(4)
ax1 = plt.subplot(211)
plt.title('Pre-filtro')
plt.plot(t,pre,'.',markersize='0.5',linewidth='1')
ax2 = plt.subplot(212, sharex=ax1, sharey=ax1)
plt.title('Post-filtro')
plt.plot(t,post,'.',markersize='0.5',linewidth='1')
plt.subplots_adjust(hspace=0.4)

#%% FIGURA

def applyPlotStyle():
    plt.xlabel('Tiempo (s)',fontsize=18)
    plt.ylabel('Voltaje (V)',fontsize=18)
    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)
    plt.legend()
    
offset = 18
ventana = 5
    
plt.figure(470)
plt.plot(t-offset, post, linewidth='0.8',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([0.2,0.25])
applyPlotStyle()
plt.show()

#%% MASCARA

nf = '24PC/dormido/47ohm_mascara.txt'
data = np.loadtxt(nf,skiprows=1)

#%% RAW

t = data[:,0]/1000

pre = data[:,1]/1000
post = data[:,2]/1000

def applyPlotStyle():
    plt.ylabel('Voltaje (V)',fontsize=14)
    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=12)
    plt.rc('ytick',labelsize=12)
    plt.legend()

plt.figure(4)
ax1 = plt.subplot(211)
plt.title('RAW',loc='right',weight='bold',fontsize=18)
plt.plot(t,pre,linewidth='0.8',color = 'royalblue')
applyPlotStyle()

ax2 = plt.subplot(212, sharex=ax1, sharey=ax1)
plt.title('LOW-PASS 2000 Hz',loc='right',weight='bold',fontsize=18)
plt.plot(t,post,linewidth='0.8',color = 'royalblue')
plt.xlabel('Tiempo (s)',fontsize=14)
applyPlotStyle()



plt.subplots_adjust(hspace=0.8)
plt.show()

#%% FIGURA

def applyPlotStyle():
    plt.xlabel('Tiempo (s)',fontsize=18)
    plt.ylabel('Voltaje (V)',fontsize=18)
    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)
    plt.legend()
    
offset = 5  
ventana = 5
    
plt.figure(471)
plt.plot(t-offset, post, linewidth='0.8',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([0.2,0.25])
applyPlotStyle()
plt.show()