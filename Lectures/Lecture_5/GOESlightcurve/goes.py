# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 13:26:40 2018
https://umbra.nascom.nasa.gov/goes/fits/2018/
use FV.exe to analyze structure of the file 
Lecture 5.1/5 Read and plot light curve from GOES FIT-file
@author: cmonstei
"""
#----------------------------------------------------------------------------
import numpy as np
import pyfits as pf
from matplotlib import pyplot as plt
#----------------------------------------------------------------------------

myfile    = 'go1520180122.fits'
hdu       = pf.open(myfile)
flux1     = hdu[2].data[0][1][:,0]
flux2     = hdu[2].data[0][1][:,1]
date      = hdu[0].header['DATE-OBS']
time      = hdu[0].header['TIME-OBS']
unit      = hdu[2].header['TUNIT2']
telescope = hdu[2].header['TELESCOP']

print hdu.info() # FIT-file structure

dT = 2.048 # exposure time [s], see https://umbra.nascom.nasa.gov/goes/fits/goes_fits_files_notes.txt
taxis = np.arange(0, flux1.size, 1) * dT

plt.figure(figsize=(12,8))
plt.plot(taxis,flux1,color='r')
plt.plot(taxis,flux2,color='b')
plt.xlabel('Time [s]',fontsize=15)
plt.ylabel('Flux ['+unit+']',fontsize=15)
plt.xlim(0,84000)
plt.ylim(1e-9,1e-5)
plt.yscale('log')
plt.title(telescope+' of '+date+' at '+time,fontsize=15)
plt.tick_params(labelsize=14)
plt.grid(axis='both')
plt.savefig(myfile + ".png")
plt.show()
hdu.close()
#----------------------------------------------------------------------------
