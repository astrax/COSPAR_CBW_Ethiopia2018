# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 19:23:25 2018
http://scipyscriptrepo.com/wp/?p=76
pip install lmfit
Lecture 5.2/5 Gauss fit
@author: STEG
"""

import numpy as np
import pyfits as pf
import matplotlib.pyplot as plt
from lmfit import  Model

#-------------------------------------------------------------------------------------------
plt.figure(figsize=(10,7))

myfile = 'go1520180122.fits'
hdu    = pf.open(myfile)
flux1  = hdu[2].data[0][1][:,0]
flux2  = hdu[2].data[0][1][:,1]

date      = hdu[0].header['DATE-OBS']
time      = hdu[0].header['TIME-OBS']
unit      = hdu[2].header['TUNIT2']
telescope = hdu[2].header['TELESCOP']

print hdu.info() # FIT-file structure
dT = 2.048 # exposure time [s], see https://umbra.nascom.nasa.gov/goes/fits/goes_fits_files_notes.txt
taxis = np.arange(0, flux1.size, 1) * dT
plt.plot(taxis,flux1)
plt.xlabel('Time [s]')
plt.ylabel('Flux ['+unit+']')
plt.xlim(5000,20000) #84000
plt.ylim(0,1e-6)
#plt.yscale('log')
plt.title(telescope+' of '+date+' at '+time)

mask = ((taxis>11000)*(taxis<16000)) 
flux = flux1[mask]
time = taxis[mask]
plt.plot(time,flux,'.r')
plt.grid(axis='both')
plt.tight_layout()
#-------------------------------------------------------------------------------------------

plt.figure(figsize=(10,7))

def gaussian(x, amp, cen, wid):
    "1-d gaussian: gaussian(x, amp, cen, wid)"
    return (amp/(np.sqrt(2*np.pi)*wid)) * np.exp(-(x-cen)**2 /(2*wid**2))

gmodel = Model(gaussian)
result = gmodel.fit(flux, x=time, amp=1e-6, cen=11000, wid=2000)

print(result.fit_report())

plt.plot(time, flux,         'b')
plt.plot(time, result.best_fit, 'r')
plt.xlabel('Time [s]')
plt.ylabel('Flux ['+unit+']')
plt.grid(axis='both')
plt.tight_layout()
plt.show()
