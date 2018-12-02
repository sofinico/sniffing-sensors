import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import butter, lfilter

data = np.loadtxt('primera_invivo_sinolor.txt', skiprows = 1)

#%%

t = data[:,0]
v = data[:,1]
del data

#%%

i = len(t)//3
f = len(t)//3 + len(t)//3

nt = t[i:f]
nv = v[i:f]

plt.plot(nt,nv,'-',linewidth = 0.5)

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

y = butter_lowpass_filter(nv, cutoff, fs, order)

plt.figure(244)
#plt.plot(t, v, 'b-', label='data',linewidth='0.5')
plt.plot(nt, y, linewidth='0.5')
plt.show()

