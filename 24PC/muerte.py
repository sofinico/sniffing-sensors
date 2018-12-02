#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz

muerte = np.loadtxt('datos-L6/muerte.txt',skiprows=0)

#%% RAW DATA

t = muerte[:,0]
v = muerte[:,1]

plt.figure(10)
plt.plot(t,v,linewidth='0.5')
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
fs = 30000    # sample rate, Hz
cutoff = 2000  # desired cutoff frequency of the filter, Hz

#%% GRAFICO

offset = 25.5
ventana = 2
t = muerte[:,0]-offset
v = muerte[:,1]

def applyPlotStyle():
    plt.xlabel('Tiempo (s)',fontsize=18)
    plt.ylabel('Voltaje (V)',fontsize=18)
    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)
    plt.legend()

y = butter_lowpass_filter(v, cutoff, fs, order)

plt.figure(23)
plt.plot(t, y, 'g-', linewidth='0.8',color = 'royalblue')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([0.5,3])
applyPlotStyle()
plt.show()


