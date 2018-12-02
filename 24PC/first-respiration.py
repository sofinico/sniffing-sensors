#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz

first = np.loadtxt('24PC/dormido-L6/18710000.txt',skiprows=1)
first3 = np.loadtxt('24PC/dormido-L6/18710003.txt',skiprows=1)
first4 = np.loadtxt('24PC/dormido-L6/18710004.txt',skiprows=1)

#%% RAW DATA

t = first[:,0]
v = first[:,3]
t3 = first3[:,0]
v3 = first3[:,3]
t4 = first4[:,0]
v4 = first4[:,3]

plt.figure(1)
plt.plot(t,v,linewidth='0.5')

plt.figure(3)
plt.plot(t3,v3,linewidth='0.5')

plt.figure(4)
plt.plot(t4,v4,linewidth='0.5')
plt.show()

#%% BAJA SENSIBILIDAD

first3 = np.loadtxt('datos-L6/18710003.txt',skiprows=1)

#%% SIN FILTRAR

offset = 2.25
ventana = 2
t3 = first3[:,0]/1000-offset
v3 = first3[:,3]/1000

def applyPlotStyle():
    plt.xlabel('Tiempo (s)',fontsize=18)
    plt.ylabel('Voltaje (V)',fontsize=18)
    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)
    plt.legend()
    
    
plt.figure(24)
plt.plot(t3, v3, 'g-', linewidth='0.3',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([3.697,3.705])
applyPlotStyle()
plt.show()

#%% FILTROS

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

order = 6
fs = 30000   # sample rate, Hz
cutoff = 2000  # desired cutoff frequency of the filter, Hz

#%% GRAFICO

y = butter_lowpass_filter(v3, cutoff, fs, order)

plt.figure(244)
#plt.plot(t, v, 'b-', label='data',linewidth='0.5')
plt.plot(t3, y, 'g-', linewidth='0.5')
plt.xlim([2.25,4.25])
plt.ylim([3.705,3.695])
applyPlotStyle()
plt.show()

