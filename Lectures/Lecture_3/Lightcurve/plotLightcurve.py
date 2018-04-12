# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 12:02:42 2016
Lecture 3.2/5 How to plot light curves
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
plt.ylabel('Frequency [channel number]',fontsize=15)
plt.title('FIT file presentation as original raw data, full size',fontsize=15)
plt.savefig(files+'.raw.png')
plt.show()
#-----------------------------------------------------------------------------

plt.figure(figsize=(12,8))
channel = 170
title = 'Light curve at channel {:3d} = {:5.1f} MHz'.format(channel,freqs[channel])

lc1 = data[channel,:] # select channel near burst
lc1 = smooth(lc1,3)
lc0 = lc1[5] # get lowest value (try)
dB2 = (lc1-lc0)/255.0 * 2500.0/25.4 # converter into dB

plt.plot(time,dB2)
plt.tick_params(labelsize=14)
plt.xlabel('Sampling time [s] of '+files,fontsize=15)
plt.ylabel('Intensity [dB]',fontsize=15)
plt.title(title,fontsize=15)
plt.grid(axis='both')
plt.ylim(-2,10)
plt.xlim(0,900)
plt.savefig(files+'.LigthCurve170.png')
plt.show()

fds.close()
#-----------------------------------------------------------------------------
