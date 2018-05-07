# -*- coding: utf-8 -*-
"""
Created on Thu May 03 16:11:28 2018

@author: Ahmed
Source for help:
    1) Sunpy docs: http://docs.sunpy.org/en/stable/guide/acquiring_data/fido.html
    2) VSO site for attrs keys: https://sdac.virtualsolar.org/cgi/show_details?instrument=SECCHI
"""
from __future__ import print_function, division
import astropy.units as u
from sunpy.net import Fido, attrs as a
import matplotlib.pyplot as plt
import sunpy.map
#%% Download SDO AIA data
## aia

#result = Fido.search(a.Time('2017/9/06 14:05', '2017/9/06 14:10'),
#                     a.Instrument('aia'),
#                     a.Wavelength(171*u.angstrom) | a.Wavelength(94*u.angstrom))
#print(result)
#downloaded_files = Fido.fetch(result, path='../data/{instrument}/{file}')
#print(downloaded_files)

## Magnetometer HMI

#result = Fido.search(a.vso.Source('SDO') &
#          a.Instrument('HMI') &
#          a.Time('2011-01-01', '2011-01-01T00:01:00'))
#print(result)
#downloaded_files = Fido.fetch(result, path='../data/{instrument}/{file}')
#print(downloaded_files)


#%% Download stereo data

#stereo = Fido.search(a.vso.Source('STEREO_A') &
#          a.Instrument('COR2') &
#          a.Time('2011-01-01', '2011-01-01T00:10:00'))
#print(stereo)
#downloaded_files = Fido.fetch(stereo, path='../data/{instrument}/{file}')
#print(downloaded_files)

#%% plot example file

#COR1 = sunpy.map.Map('../data/SECCHI/20110101_000500_s4c1a.fts')
#fig = plt.figure()
#COR1.plot()
#plt.colorbar()
#
#COR2 = sunpy.map.Map('../data/SECCHI/20110101_000915_n4c2a.fts')
#fig = plt.figure()
#COR2.plot()
#plt.colorbar()
#plt.show()
