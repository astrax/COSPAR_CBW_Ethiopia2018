# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 19:23:25 2018
http://www.scipy-lectures.org/intro/summary-exercises/optimize-fit.html
y = a + b*(t-to) + c*(t-to)**2 + d*(t-to)**3
Lecture 5.5/5 polynominal fit with 5 coefficients, add titles and labels
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

date      = hdu[0].header['DATE-OBS']
time0     = hdu[0].header['TIME-OBS']
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
plt.title(telescope+' of '+date+' at '+time0)

mask = ((taxis>11000)*(taxis<16000)) 
flux = flux1[mask]
time = taxis[mask]
plt.plot(time,flux,'.r')
plt.grid(axis='both')
plt.tight_layout()

#-------------------------------------------------------------------------------------------

plt.figure(figsize=(10,7))

def model(t, coeffs):
   return coeffs[0] + coeffs[1] * (t-coeffs[4]) + coeffs[2] * (t-coeffs[4])**2 + coeffs[3] * (t-coeffs[4])**3

guess = np.array([2e-8, 0, 0, 1e-8, 11000], dtype=float) # initial guess
def residuals(coeffs, y, t):
    return y - model(t, coeffs)
    
x, flag = leastsq(residuals, guess, args=(flux, time))
print(x)
    
plt.plot(time, flux, time, model(time, x), 'r')
plt.xlabel('Time [s]',fontsize=15)
plt.ylabel('Flux ['+unit+']',fontsize=15)
plt.title(telescope+' of '+date+' at '+time0,fontsize=15)
plt.text(14000,8e-7,'Blue = Fluxdata',color='blue',fontsize=15)
plt.text(14000,7e-7,'Red  = Polynom 5th degree',color='red',fontsize=15)
plt.grid(axis='both')
plt.tight_layout()

plt.show()
#-------------------------------------------------------------------------------------------
