# -*- coding: utf-8 -*-
"""
Created on Tue JUL 19 2016
Updated on Thu OCT 19 2017
Lectre 3.3/5 Flip y-axis of 2D-plot (spectrum)
@author: Christian Monstein
"""

import pyfits
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm

#------------------------------------------------------------------------------
files = 'BIR_20150311_161500_02.fit.gz' # local data file
#------------------------------------------------------------------------------

hdu = pyfits.open(files)
print hdu.info() # FIT-file structure

dB = hdu[0].data.astype(np.float32)/255.0*2500.0/25.4 # conversion digits -> dB
mini_dB = np.min(dB) # find lowest value
rel_dB = dB - mini_dB # set background 0

freqs = hdu[1].data['Frequency'][0] # extract frequency axis
time  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

rel_dB = rel_dB - rel_dB.mean(axis=1, keepdims=True)  # subtract average 
rel_dB = rel_dB.clip(-2,12) # limit peak values +/-
#------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
extent = (time[0], time[-1], freqs[-1], freqs[0])
plt.imshow(rel_dB, aspect = 'auto', extent = extent, cmap=cm.inferno_r) 
## cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
plt.tick_params(labelsize=14)
plt.xlabel('Time [s] of '+files,fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file presentation as original raw data, full size',fontsize=15)

plt.savefig('2D_original.png')
plt.savefig('2D_original.eps', bbox_inches='tight', pad_inches=0, dpi=50,orientation='landscape')

#------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
rel_dB = np.flipud(rel_dB)
extent = (time[0], time[-1], freqs[0], freqs[-1])
plt.imshow(rel_dB, aspect = 'auto', extent = extent, cmap=cm.jet) 
## cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
plt.tick_params(labelsize=14)
plt.xlabel('Time [s] of '+files,fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file presentation as flipped raw data, full size',fontsize=15)

plt.savefig('2D_flipud.png')

#------------------------------------------------------------------------------
