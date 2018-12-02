#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz


pipeta = np.loadtxt('datos-L6/18706004.txt',skiprows=1)

#%% RAW DATA

t = pipeta[:,0]
v = pipeta[:,3]

plt.figure(66)
plt.plot(t,v,linewidth='0.5')
plt.show()


