#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

#%% DIRECTO

nf = 'datos/470ohm_directo.txt'
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
    
offset = 4
ventana = 10
    
plt.figure(4700)
plt.plot(t-offset, post, linewidth='0.8',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([1.655,1.675])
applyPlotStyle()
plt.show()

#%% MANGUERA

nf = 'datos/470ohm_manguera.txt'
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
    
offset = 23
ventana = 10
    
plt.figure(4701)
plt.plot(t-offset, post, linewidth='0.8',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([1.6,1.7])
applyPlotStyle()
plt.show()

#%% MASCARA

nf = 'datos/470ohm_mascara.txt'
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
    
offset = 2.5
ventana = 10
    
plt.figure(4702)
plt.plot(t-offset, post, linewidth='0.8',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([1.6,1.7])
applyPlotStyle()
plt.show()

#%% TRESHOLD

#def applyPlotStyle():
    #plt.xlabel('Ventana temporal (s)',fontsize=18)
    #plt.ylabel('Voltaje (V)',fontsize=18)
    #plt.grid(linestyle=':',color = 'lightgrey')
    #plt.rc('xtick',labelsize=14)
    #plt.rc('ytick',labelsize=14)
    #plt.legend(loc='best')
    
offset = 8
ventana = 2
    
plt.figure(4702)
plt.hlines(np.mean(post[150000:200000]),0,2,
           color='black',linestyle='dotted',label='Promedio')
plt.plot(t-offset, post, linewidth='1.5',color = 'black')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([1.65,1.675])
plt.show()

#%% SIMIL CANULA

nf = 'datos/470ohm_similcanula.txt'
data = np.loadtxt(nf,skiprows=1)

#%% RAW

t = data[:,0]/1000

post = data[:,1]*0.03/1000 + 1.662

plt.figure(5000)
plt.title('Post-filtro')
plt.plot(t,post,'.',markersize='0.5',linewidth='1')
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
ventana = 10
    
plt.figure(4703)
plt.plot(t-offset, post, linewidth='0.8',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([1.6,1.7])
applyPlotStyle()
plt.show()

#%% SPECTRUM SIMIL CANULA

nf = 'datos/spectrum_similcanula.txt'
data = np.loadtxt(nf,skiprows=1)

#%% RAW

f = data[:,0]

spect = data[:,1]

plt.figure(5000)
plt.plot(f,spect,'-',markersize='0.5',linewidth='1')
plt.show()

#%% FIGURA

def applyPlotStyle():
    plt.xlabel('Frecuencia (Hz)',fontsize=18)
    plt.ylabel('Espectro (dB)',fontsize=18)
    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)
    plt.legend(fontsize=14,loc='best')
    
plt.figure(4700)
plt.vlines(2.44,-50,60,color='grey',linestyle='solid',label='2.44 Hz')
plt.plot(f, spect, linewidth='0.8', color='royalblue')
plt.ylim([-30,60])
applyPlotStyle()
plt.show()


