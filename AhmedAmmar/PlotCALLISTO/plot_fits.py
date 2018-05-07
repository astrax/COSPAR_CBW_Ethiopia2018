# -*- coding: utf-8 -*-
"""
Created on Fri May 04 20:47:20 2018
@author: Ahmed
Purpose: Plot e-CALLISTO data
Source for help:
"""

from sunpy.spectra.sources.callisto import CallistoSpectrogram
import matplotlib.pyplot as plt

files = '..//DataCALLISTO//GREENLAND_20170906_121001_63.fit.gz'

image = CallistoSpectrogram.read(files)

#plt.figure(figsize=(12,8))

image.plot()
#plt.xlim((2000,3600)) # express limits in column number 0...3599
plt.savefig(files+'_raw.png')

#plt.figure(figsize=(12,8))

img_nobg = image.subtract_bg()
img_nobg.plot(vmin=-3)
#plt.xlim((2000,3600)) # express limits in column number 0...3599

plt.savefig(files+'_nobg.png')
plt.tight_layout()
plt.show()
