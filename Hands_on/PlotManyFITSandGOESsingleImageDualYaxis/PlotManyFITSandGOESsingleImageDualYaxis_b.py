# ipython script to plot FIT-files from rfi-monitoring system
# Created: Chr. Monstein 23.07.2016

#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import pyfits as pf
import numpy as np
from astropy.io import fits
import glob

#-------------------------------------------------------------------------------
def get_data_from_fits(path):
    with fits.open(path) as hdu:
        data = hdu[0].data.astype(np.float32) # float16
    return data
    
#-------------------------------------------------------------------------------
#get paths matching criteria
#paths = glob.glob('//winhome/cmonstei/My Documents/Python/TypeII/OOTY*.fit.gz')
#paths = glob.glob('C:/Users/Hitsch/Documents/MyPython/GOES_TypeII/BLENSW*.fit.gz')
#paths = glob.glob('C:/MyPython/Ethiopia/Hands-On/PlotManyFITSandGOESsingleImage/BLENSW*.fit.gz')
paths = glob.glob('C:\Users\Hitsch\Documents\cospar2018\Hands-On\PlotManyFITSandGOESsingleImageDualYaxis/GREEN*.fit.gz')
print(len(paths))
print(paths)
FreqRange = [20,80]
TimeRange = [13.75,14.25]
#-------------------------------------------------------------------------------
# time axis
instrument = pf.open(paths[0])[0].header['INSTRUME']

# get time axis
time = pf.open(paths[0])[1].data[0][0]
date = pf.open(paths[0])[0].header['DATE-OBS']
start_time = float(pf.open(paths[0])[0].header['TIME-OBS'].split(":")[0])*60*60 + float(pf.open(paths[0])[0].header['TIME-OBS'].split(":")[1])*60 + float(pf.open(paths[0])[0].header['TIME-OBS'].split(":")[2])  
ut = time + start_time

#-------------------------------------------------------------------------------
# get frequency axis
frequency = pf.open(paths[0])[1].data[0][1]

#-------------------------------------------------------------------------------
#stack all spectrums
data_full = np.hstack([get_data_from_fits(path) for path in paths])
print(data_full.shape)

#-------------------------------------------------------------------------------
compression = 1 # 8*0.25s = 2s
dT = 0.25*compression
tt=data_full.shape[1]/compression 
ff=data_full.shape[0] # take all
data=data_full.reshape((ff,data_full.shape[0]/ff,tt,-1)).mean(axis=3).mean(1)

#-------------------------------------------------------------------------------
time_axis = (start_time + dT * np.arange(data.shape[1]))/3600.0

#-------------------------------------------------------------------------------
vmin = -1 # -0.5, 100
vmax =  6 # 4, 160
dref = data - np.min(data)
dB = dref/255.0*2500.0/25.4 # conversion into dB
dB_median = np.median(dB, axis=1,keepdims=True)
dBflat = dB-dB_median
#-------------------------------------------------------------------------------

plt.figure(figsize=(15,8))
ax1 = plt.gca()

ax1.imshow(dBflat, 
           aspect="auto", 
           cmap="gist_heat_r", # afmhot, CMRmap, gnuplot, rainbow, hot, hot_r, magma, inferno, plasma, jet, cubehelix
           extent=[time_axis[0], time_axis[-1], frequency[-1], frequency[0]],
           norm=plt.Normalize(vmin, vmax)
          )
#plt.colorbar(label="dB above background")
ax1.set_xlabel("Time [UT]",fontsize=16)
ax1.set_ylabel("Callisto plasma frequency [MHz]",fontsize=16)
ax1.set_title(date + ' ' + instrument + ' Type II and GOES-14.', fontsize=16)
ax1.set_xlim(TimeRange) # UT
ax1.set_ylim(FreqRange) # MHz
ax1.set_xticks(np.arange(min(time_axis), max(time_axis)+0, 0.3))
ax1.set_xticklabels(time_axis,fontsize=14)
ax1.set_yticklabels(frequency,fontsize=14)

start, end = ax1.get_xlim()
ax1.xaxis.set_ticks(np.arange(start, end, 0.05))
ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

start, end = ax1.get_ylim()
ax1.yaxis.set_ticks(np.arange(start, end, 5))
ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

#-------------------------------------------------------------------------------

myfile    = 'go1420160504.fits'
hdu       = pf.open(myfile)
flux1     = hdu[2].data[0][1][:,0]
flux2     = hdu[2].data[0][1][:,1]
date      = hdu[0].header['DATE-OBS']
time      = hdu[0].header['TIME-OBS']
unit      = hdu[2].header['TUNIT2']
telescope = hdu[2].header['TELESCOP']

print hdu.info() # FIT-file structure

dT = 2.048 # exposure time [s], see https://umbra.nascom.nasa.gov/goes/fits/goes_fits_files_notes.txt
taxis = np.arange(0, flux1.size, 1) * dT / 3600.

ax2 = ax1.twinx()
ax2.plot(taxis,flux1,'r--',linewidth=3.0)
ax2.plot(taxis,flux2,'b--',linewidth=3.0)
ax2.set_ylabel(telescope+'  ['+unit+']',fontsize=15)

ax2.set_yticklabels(flux1,fontsize=14)
start, end = ax2.get_ylim()
ax2.yaxis.set_ticks(np.arange(0, end, 1e-7)) # -6
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%3.1e'))
ax2.set_xlim(TimeRange)

hdu.close()
ax1.autoscale(False)
ax2.autoscale(False)

ax1.plot(14., 75, label='0.5-4.0 A',color='b')
ax1.plot(14., 70, label='1.0-8.0 A',color='r')

ax1.legend()

plt.show()

plt.savefig("GOESand TypeII_%s_b.jpg"%(date.replace("/", "_")),
            bbox_inches="tight")

#-------------------------------------------------------------------------------
