# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:34:12 2018
Search your file of interest here: http://soleil.i4ds.ch/solarradio/callistoQuicklooks/
Save file in the local folder data
Lecture 2.9b/5 Pseudo calibration and black background

@author: Christian Monstein
"""


import pyfits
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
 
mypath = 'C:/Users/Hitsch/Documents/cospar2018/Lecture_2/data/'
mypath = 'C:/MyPython/Ethiopia/Lectures/Lecture_2/data/'
mypath = 'C:/Users/Hitsch/Documents/cospar2018/Lectures/Lecture_2/data/'

myfile = 'ALMATY_20110809_080000_59.fit.gz'

hdu   = pyfits.open(mypath + myfile)
data  = hdu[0].data.astype(np.float32)
freqs = hdu[1].data['Frequency'][0] # extract frequency axis
time  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

#------------------------------------------------------------------------------
fig=plt.figure(figsize=(12,8))
extent = (time[0], time[-1], freqs[-1], freqs[0])

fig.patch.set_facecolor('black')
bgs_methode = 1
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

plt.imshow(dB, aspect = 'auto', extent = extent, cmap=cm.CMRmap, vmin=-4,vmax=15) 
# cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
# cm.gnuplot, cm.gnuplot2, cm.CMRmap, cm.plasma, cm.magma
plt.tick_params(labelsize=14,colors='white')
plt.xlabel('Time [s] of FIT-file: ' + myfile,fontsize=15,color='white')
plt.ylabel('Plasma frequency [MHz]',fontsize=15,color='white')
plt.title('FIT file average spectrum subtracted and pseudo calibrated.',fontsize=15,color='white')

cbar = plt.colorbar()
cbar.ax.set_ylabel('dB above background',fontsize=15,color='white')
plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='white',fontsize=12)

plt.savefig(myfile + "_bbg.png", facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
#------------------------------------------------------------------------------