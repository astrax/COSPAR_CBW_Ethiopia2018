# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:34:12 2018
Calibration in dB above background
Colorbar in dB
Lecture 2.9a/5 Pseudo calibration

@author: Christian Monstein
"""


import pyfits
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
 
mypath = 'C:/Users/Hitsch/Documents/cospar2018/Lecture_2/data/'
mypath = 'H:\My Documents\COSPAR2018\Lectures\Lecture_2\data/'
mypath = 'C:/MyPython/Ethiopia/Lectures/Lecture_2/data/'
mypath = 'C:/Users/Hitsch/Documents/cospar2018/Lectures/Lecture_2/data/'

myfile = 'ALMATY_20110809_080000_59.fit.gz'

hdu   = pyfits.open(mypath + myfile)
data  = hdu[0].data.astype(np.float32)
freqs = hdu[1].data['Frequency'][0] # extract frequency axis
time  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

#------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
extent = (time[0], time[-1], freqs[-1], freqs[0])

bgs_methode = 0
if (bgs_methode==1):
    timemarker=5
    ref =  data[:,timemarker]
    bgs = np.transpose(np.transpose(data) - ref)  # subtract average 
else:
    bgs = data - data.mean(axis=1, keepdims=True)  # subtract average 

digitrange   = 255.0  # digit
voltagerange = 2500.0 # mV
sensitivity  = 25.4   # mV/dB
dB = bgs/digitrange * voltagerange/sensitivity

plt.imshow(dB, aspect = 'auto', extent = extent, cmap=cm.gnuplot2, vmin=-4,vmax=15) 
# cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
# cm.gnuplot, cm.gnuplot2, cm.CMRmap, cm.plasma, cm.magma
plt.tick_params(labelsize=14)
plt.xlabel('Time [s] of FIT-file: ' + myfile,fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file average spectrum subtracted and pseudo calibrated.',fontsize=15)

cbar = plt.colorbar()
cbar.ax.set_ylabel('dB above background',fontsize=15)

plt.savefig(myfile + ".png")
#------------------------------------------------------------------------------