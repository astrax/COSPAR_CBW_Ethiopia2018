# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 12:02:42 2016
Lecture 3.1/5 How to plot light curve(s)
@author: cmonstei
"""

import pyfits
import matplotlib.pyplot as plt 
import numpy as np
#-----------------------------------------------------------------------------
def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth
#-----------------------------------------------------------------------------

files = 'BLEN5M_20151104_140000_01.fit.gz'

fds = pyfits.open(files)

data  = fds[0].data
freqs = fds[1].data['Frequency'][0] # extract frequency axis
time  = fds[1].data['Time'][0] # extract time axis
#-----------------------------------------------------------------------------

plt.figure(figsize=(12,8))
extent = (time[0], time[-1], freqs[-1], freqs[0])
plt.imshow(data, extent = extent, aspect = 'auto',cmap='jet')
# cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
plt.tick_params(labelsize=14)
plt.xlabel('Sampling time [s] of '+files,fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file presentation as original raw data, full size',fontsize=15)
plt.savefig(files+'.raw.png')
plt.show()
#-----------------------------------------------------------------------------

plt.figure(figsize=(12,8))
pixel1 = 1900
pixel0 = 100
title = 'Single spectrum at T={:5.1f} sec'.format(time[pixel1])
sp1 = data[:,pixel1] # select channel near burst
sp0 = data[:,pixel0] # select channel far away from burst
dB = (sp1-sp0)/255.0*2500.0/25.4
plt.plot(freqs,dB,'-r',linewidth=3.0)
plt.tick_params(labelsize=14)
plt.xlabel('Plasma frequency [MHz] of: '+files,fontsize=15)
plt.ylabel('Intensity [dB] above quiet sun',fontsize=15)
plt.title(title,fontsize=15)
plt.grid(axis='both')
plt.ylim(0,15)
plt.xlim(980,1250)
plt.savefig(files+'.Spectrum.png')
plt.show()

fds.close()
#-----------------------------------------------------------------------------
