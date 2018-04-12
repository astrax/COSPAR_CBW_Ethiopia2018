# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 19:23:25 2018
http://www.scipy-lectures.org/intro/summary-exercises/optimize-fit.html
Lecture 5.6/5 nonlinear logarithmic fit with 2 coefficients, add titles and labels
@author: STEG
"""
#-------------------------------------------------------------------------------------------

import numpy as np
import pyfits as pf
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

#-------------------------------------------------------------------------------------------
plt.figure(figsize=(10,7))

myfile = 'go1520180122.fits'
hdu    = pf.open(myfile)
flux1  = hdu[2].data[0][1][:,0]
flux2  = hdu[2].data[0][1][:,1]

Date      = hdu[0].header['DATE-OBS']
Time      = hdu[0].header['TIME-OBS']
Unit      = hdu[2].header['TUNIT2']
Telescope = hdu[2].header['TELESCOP']

print hdu.info() # FIT-file structure
dT = 2.048 # exposure time [s], see https://umbra.nascom.nasa.gov/goes/fits/goes_fits_files_notes.txt
taxis = np.arange(0, flux1.size, 1) * dT
plt.plot(taxis,flux1)
plt.xlabel('Time [s]')
plt.ylabel('Flux ['+Unit+']')
plt.xlim(5000,20000) #84000
plt.ylim(0,1e-6)
#plt.yscale('log')
plt.title(Telescope+' of '+Date+' at '+Time)

mask = ((taxis>9200)*(taxis<18000)) # mask out sub-set of data
flux = flux1[mask]
time = taxis[mask]
plt.plot(time,flux,'.r')
plt.grid(axis='both')
plt.tight_layout()

#-------------------------------------------------------------------------------------------

def MyModel(t, coeffs):
   return coeffs[0]/(((t-coeffs[1])/coeffs[2]))**(1.+np.log((t-coeffs[1])/coeffs[2]))

#-------------------------------------------------------------------------------------------

def residuals(coeffs, y, t):
    return y - MyModel(t, coeffs)
#-------------------------------------------------------------------------------------------

Pinitial = np.array([4.0e-07, 8.0e+03,2.7e+03], dtype=float) # initial guess    
Pfinal, flag = leastsq(residuals, Pinitial, args=(flux, time))
   
plt.figure(figsize=(10,7))
plt.plot(time, flux, 'r')
plt.plot(time, MyModel(time, Pfinal), 'b')

plt.grid(axis='both')
plt.xlabel('Time [s]')
plt.ylabel('Flux ['+Unit+']')
plt.title(Telescope+' of '+Date+' at '+Time)
plt.tight_layout()

plt.show()

print (Pfinal)
#-------------------------------------------------------------------------------------------
