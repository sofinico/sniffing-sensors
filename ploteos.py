# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:59:28 2018

@author: noelp
"""

import matplotlib.pyplot as plt
import numpy as np
#%%

'''
Filtro con ventana de 200ms
'''

data1 = np.loadtxt('cerca exhalacion positiva  filtro lento Picos.txt', skiprows=1)
#labels1 = ['tPicoInh(ms)', 'voltajePicoInh', 'tInicioInh(ms)', 'voltajeInicioInh',  'tFinInh(ms)', 'voltajeFinInh']

data = np.loadtxt('cerca exhalacion positiva filtro lento.txt', skiprows=1)
#labels =['t(ms)',  'voltaje(mV)',  'filtroGolay', 'detrend'] 

#%%

'''
Filtro con ventana de 100ms
'''

data1 = np.loadtxt('cerca exhalacion positiva Picos.txt', skiprows=1)
#labels = ['tPicoInh(ms)', 'voltajePicoInh', 'tInicioInh(ms)', 'voltajeInicioInh',  'tFinInh(ms)', 'voltajeFinInh']

data = np.loadtxt('cerca exhalacion positiva.txt', skiprows=1)
#labels = ['t(ms)',  'voltaje(mV)', 'filtroGolay', 'detrend']

#%%


tfl = data1[:,0]/1000; vpinh = data1[:,1]
tinh0 = data1[:,2]/1000; vinh0 = data1[:,3]
tinhf = data1[:,4]/1000; vinhf = data1[:,5]

t = data[:,0]/1000; v = data[:,1]; filt = data[:,2]; detr = data[:,3]


#%%


def applyPlotStyle(xlabel, ylabel):
    plt.xlabel(xlabel,fontsize=15)
    plt.ylabel(ylabel,fontsize=15)
#    plt.grid(linestyle=':',color = 'lightgrey')
    plt.rc('xtick',labelsize=14)
    plt.rc('ytick',labelsize=14)
    plt.tight_layout()
#%%

def axis():
    plt.axhline(y=0.58,xmin=0.25,xmax=0.5, color='lightgrey', linewidth='5')
    plt.text(0.5,0.6,'0.5 seg', fontsize=12)
    plt.axvline(x=0.25,ymin=0.77,ymax=0.9,color='lightgrey',linewidth='5')
    plt.text(0.35,0.45,'2mV', fontsize=12, rotation=90)

#%%
    
runfile('C:/Users/noelp/Documents/Facultad/Exactas/Laboratorio/LABO 6-7/escala.py')

fitfunc(p1,v)

vpinh = fitfunc(p1,vpinh)
vinh0 = fitfunc(p1,vinh0)
vinhf = fitfunc(p1,vinhf)
v = fitfunc(p1,v)
filt = fitfunc(p1,filt)
detr = fitfunc(p1,detr)



#%%

#offset = 6.4
offset = 16
ventana = 9


'''
Detrend
'''
plt.figure(34902,figsize=(7.5,5))
ax1 = plt.subplot(211)
plt.title('datos filtrados', loc='right', fontsize=16)
plt.axhline(y=np.average(filt), color='lightgrey', linewidth='2', linestyle='-')
plt.plot(t-offset,filt,'k-', linewidth='2')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([943,951])
applyPlotStyle('Tiempo (s)','Voltaje (mV)')
ax2 = plt.subplot(212, sharex=ax1)
plt.title('procesado detrend', loc='right', fontsize=16)
plt.axhline(y=0, color='lightgrey', linewidth='2', linestyle='-')
plt.plot(t-offset,detr,'k-',linewidth='2')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.ylim([-3,5])
plt.subplots_adjust(hspace=0.4)
applyPlotStyle('Tiempo (s)','Voltaje (mV)')
plt.show()
    
#%%
'''
Comparación final
'''
offset = 6.4
ventana = 6

plt.figure(4,figsize=(7.5,5))
ax1 = plt.subplot(211)
plt.title('datos crudos', loc='right', fontsize=16)
plt.plot(t-offset,v,'k-',linewidth='0.2', label='datos crudos')
plt.xlim([i-offset for i in [offset,offset+ventana]])
applyPlotStyle('Tiempo (s)','Voltaje (mV)')
ax2 = plt.subplot(212, sharex=ax1)
plt.title('datos procesados', loc='right', fontsize=16)
plt.plot(t-offset,detr,'k-',linewidth='2', label= 'datos procesados')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.subplots_adjust(hspace=0.4)
applyPlotStyle('Tiempo (s)','Voltaje (mV)')

plt.show()

#%%

offset = 0
ventana = 2

'''
Picos
'''
plt.figure(2390, figsize=(7.5,5))
plt.axhline(y=0, color='lightgrey', linewidth='2', linestyle='-')
plt.plot(t-offset,detr,'k-', linewidth='2')
plt.plot(tfl-offset, vpinh,'kx', markersize='8', label='Máximo')
plt.plot(tinh0-offset, vinh0,'go',markersize='8', label='Inicio')
plt.plot(tinhf-offset, vinhf,'bo',markersize='8', label='Fin')
plt.xlim([i-offset for i in [offset,offset+ventana]])
#plt.ylim([-0.1,0.68])
#plt.axis('off')
plt.title('ciclo respiratorio', loc='right', fontsize=16)
plt.legend(loc='best')
applyPlotStyle('Tiempo (s)','Voltaje (mV)')
plt.show()  

#%%

'''
Filtro Golay
'''
offset = 0
ventana = 2

plt.figure(500,figsize=(7.5,5))
plt.plot(t-offset,v,'k-',linewidth='0.5', label= 'datos crudos', alpha=0.55)
plt.plot(t-offset,filt,'k-', linewidth='2', label= 'datos filtrados')
plt.xlim([i-offset for i in [offset,offset+ventana]])
plt.title('filtro Savitzky-Golay',loc='right', fontsize=16)
plt.legend(loc='best')
applyPlotStyle('Tiempo (s)','Voltaje (mV)')
plt.show()


