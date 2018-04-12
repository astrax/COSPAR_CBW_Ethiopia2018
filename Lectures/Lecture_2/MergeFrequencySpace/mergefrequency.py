# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:34:12 2018
Search your file of interest here: http://soleil.i4ds.ch/solarradio/callistoQuicklooks/
Save file in the local folder of the Python script
Lecture 2.7/5 Merge spectra in frequency space

@author: Christian Monstein
"""



import pyfits
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
 
myfile1 = 'BIR_20110809_080000_59.fit.gz'

hdu    = pyfits.open(myfile1)
data1  = hdu[0].data.astype(np.float32)
freqs1 = hdu[1].data['Frequency'][0] # extract frequency axis
time1  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

myfile2 = 'ALMATY_20110809_080000_59.fit.gz'

hdu    = pyfits.open(myfile2)
data2  = hdu[0].data.astype(np.float32)
freqs2 = hdu[1].data['Frequency'][0] # extract frequency axis
time2  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

data = np.concatenate((data2[17:182,:], data1[10:178,:]))
time = time1
freqs=np.hstack((freqs2[17:182],freqs1[10:178]))
#------------------------------------------------------------------------------
fig=plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

extent = (time[0], time[-1], freqs[-1], freqs[0])

bgs = data -  data.mean(axis=1, keepdims=True)  # subtract average

ax.imshow(bgs, aspect = 'auto', extent = extent, cmap=cm.plasma, vmin=-1,vmax=40) 
# cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
# cm.gnuplot, cm.gnuplot2, cm.CMRmap, cm.plasma, cm.magma
yticks = plt.gca().get_yticks().tolist() # get list of ticks
#yticks[-1] = ''                          # set last tick to empty string
ax.set_yticklabels([20,40,60,80,100,200,400,600,800])
#ax.set_yticklabels(yticks)
plt.tick_params(labelsize=14)
plt.xlabel('Time [s] ',fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file merge BIR/Ireland and ALMATY/Kazakhstan',fontsize=15)
plt.savefig(myfile1 +'_' +myfile2 + ".png")
plt.show()
#------------------------------------------------------------------------------