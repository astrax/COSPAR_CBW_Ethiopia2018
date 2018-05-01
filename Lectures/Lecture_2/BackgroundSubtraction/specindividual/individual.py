# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:34:12 2018
Search your file of interest here: http://soleil.i4ds.ch/solarradio/callistoQuicklooks/
Save file in the local folder of the Python script
Lecture 2.6/5 How to access data locally

@author: Christian Monstein
"""



import pyfits
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import cm
 
#mypath = 'C:/Users/Hitsch/Documents/cospar2018/Lecture_2/BackgroundSubtraction/'
#mypath = 'H:\My Documents\COSPAR2018\Lectures\Lecture_2\BackgroundSubtraction/'
#mypath = 'C:/MyPython/Ethiopia/Lectures/Lecture_2/BackgroundSubtraction/'
#mypath = 'C:/Users/Hitsch/Documents/cospar2018/Lectures/Lecture_2/BackgroundSubtraction/'

myfile = '../GAURI_20110809_075959_59.fit.gz'

#hdu   = pyfits.open(mypath + myfile)
hdu   = pyfits.open(myfile)
data  = hdu[0].data.astype(np.float32)
freqs = hdu[1].data['Frequency'][0] # extract frequency axis
time  = hdu[1].data['Time'][0] # extract time axis
hdu.close()

#------------------------------------------------------------------------------
plt.figure(figsize=(12,8))
extent = (time[0], time[-1], freqs[-1], freqs[0])
timemarker=3590  # play with me
ref =  data[:,timemarker]
bgs = np.transpose(np.transpose(data) - ref)  # subtract average 

plt.imshow(bgs, aspect = 'auto', extent = extent, cmap='gnuplot', vmin=-6,vmax=40) 
# cm.PRGn, cm.hot, cm.cool, cm.bone, cm.binary, cm.spectral, cm.jet, cm.inferno
# cm.gnuplot, cm.gnuplot2, cm.CMRmap, cm.plasma, cm.magma
plt.tick_params(labelsize=14)
plt.xlabel('Time [s] of FIT-file: ' + myfile,fontsize=15)
plt.ylabel('Plasma frequency [MHz]',fontsize=15)
plt.title('FIT file individual spectrum subtracted.',fontsize=15)
plt.savefig(myfile + ".png")
plt.show()
#------------------------------------------------------------------------------