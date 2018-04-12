# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:52:47 2018
Reads several FIT-file from directory and plots 2D spectrum with background subtracted
Left mouse click saves x-/y-coords of a FIT-file 2D-image
Left mouse event.buttion  == 1
Right mouse event.button  == 3
Wheel/thumb event.buttion == 2
Click at least two points on the spectrum
@author: Christian Monstein, ETH Zurich
"""
from matplotlib import cm
import numpy as np
from matplotlib import pyplot as plt 
import pyfits as pf
from astropy.io import fits
import glob
#-----------------------------------------------------------------------------------------------
# user input here:
MyPath = 'C:/MyPython/Ethiopia/Hands-On/InteractiveCME/' # path to the FIT-file(s)
MyPath = 'C:/Users/Hitsch/Documents/cospar2018/Hands-On/InteractiveCME/'

MyFile = 'BLENSW_20180330*_01.fit.gz' # file identification, use wildcards (*, ?)
harmonic = 2 # select excitation mode: 1=fundamental, 2=1st harmonic
newkirk  = 2 # select Newkirk model: 1.....4
zoomparameter = [700,1700,30,70] # Starttime [s], Stoptime [s], Lowfrequency [MHz], Highfrequency [MHz]y
vmin = -5 # -5.....1 minimum visible value
vmax =  25 # 4....60 maximum visible value
# play with above parameter to get best quality and zoom of the burst
#-----------------------------------------------------------------------------------------------
Rsun = 695700. # Sun radius [km]

#--------------------------------------------------------------------------------------
paths = glob.glob(MyPath+MyFile)
print '\nFIT-files found: ',(len(paths))
#print(paths)

#-------------------------------------------------------------------------------
def get_data_from_fits(path):
    with fits.open(path) as hdu:
        data = hdu[0].data.astype(np.float32) # float16
    return data
#-------------------------------------------------------------------------------

instrument = pf.open(paths[0])[0].header['INSTRUME']
date       = pf.open(paths[0])[0].header['DATE-OBS']
mytitle    = pf.open(paths[0])[0].header['CONTENT']
T0         = pf.open(paths[0])[0].header['TIME-OBS'] # start time as string
time       = pf.open(paths[0])[1].data[0][0] # time axis array
frequency  = pf.open(paths[0])[1].data[0][1] # frequency axis array

hh = float(T0.split(":")[0])
mm = float(T0.split(":")[1])
ss = float(T0.split(":")[2])
start_time = hh*3600 + mm*60 + ss # start time as float

#-------------------------------------------------------------------------------

data = np.hstack([get_data_from_fits(path) for path in paths])
print data.shape
dT = pf.open(paths[0])[0].header['CDELT1']
time_axis = (start_time + dT * np.arange(data.shape[1]))/3600.0
time_sec = (dT * np.arange(data.shape[1]))
dmean = np.mean(data, axis=1,keepdims=True)
dflat = data - dmean # subtraction background

#-------------------------------------------------------------------------------

extent = (time_sec[0],time_sec[-1], frequency[-1],frequency[0]) # range for full 2D-image

fig, ax = plt.subplots(1,figsize=(9,7))
ax.imshow(dflat, aspect = 'auto', extent = extent,cmap=cm.CMRmap,norm=plt.Normalize(vmin, vmax)) # jet, CMRmap, gnuplot2, magma, plasma
plt.xlabel("Time [s] after " + T0 + ' UT', fontsize=14)
plt.ylabel("Frequency [MHz]", fontsize=14)
plt.title(mytitle, fontsize=14)
plt.axis(zoomparameter)
plt.tick_params(axis='both', which='major', labelsize=14)
ax.autoscale = False # preventing plot from rescaling imag
#-----------------------------------------------------------------------------------------------

class MouseMonitor:
    fig = None
    axes = None

    def __init__(self, fig, ax):
        self.axes = ax
        self.fig = fig
        global coords, time, freq, Ne, rs, vr, dfdt
        coords = []
        time   = []
        freq   = []
        Ne     = []
        rs     = []
        vr     = []
        dfdt   = []

        
    def __call__(self, event):
        if event.button == 3: # right mouse click terminates action
            fig.canvas.mpl_disconnect(cid)
            plt.savefig(paths[0]+'.png')

            for i in range(len(coords)): # save all entries
                xn = coords[i][0] 
                yn = coords[i][1]
                time.append(xn)
                freq.append(yn)
                    
            for i in xrange(0,len(freq)):
                ne = (freq[i] / (harmonic*8.977e-3))**2.0 # electron density
                Ne.append(ne) # electron density
                rs.append(4.32 / (np.log10(ne/(newkirk*4.2e4)))) # radius scale
            
            plt.figure(figsize=(14,7))
            if (harmonic<2):
                st = ' , Newkirk model={:1.0f},'.format(newkirk) + ' fundamental'
            else:
                st = ' , Newkirk model={:1.0f},'.format(newkirk) + ' 1st harmonic'
            plt.suptitle('CME speed analysis of ' + paths[0] + st, fontsize=12)
            plt.subplot(2,3,1)
            plt.plot(time,freq,'-o',color="red")
            plt.grid()
            plt.xlabel("Time [s]")
            plt.ylabel("Plasma frequency [MHz]")
            
            plt.subplot(2,3,2)
            dfdt = np.abs(np.diff(freq) / np.diff(time))
            plt.plot(time[:-1],dfdt,'-o',color="green")
            plt.grid()
            plt.xlabel("Time [s]")
            plt.ylabel("df/dt [MHz/s]")
            
            plt.subplot(2,3,3)
            plt.plot(time,rs,'-o',color="blue")
            plt.grid()
            plt.xlabel("Time [s]")
            plt.ylabel("Height [Rsun]")
            
            plt.subplot(2,3,4)
            plt.plot(rs,freq,'-o',color="magenta")
            plt.grid()
            plt.ylabel("Plasma frequency [MHz]")
            plt.xlabel("Height [Rsun]")
    
            plt.subplot(2,3,5)
            plt.plot(rs[:-1],dfdt,'-o',color="cyan")
            plt.grid()
            plt.ylabel("Drift [MHz/s]")
            plt.xlabel("Height [Rsun]")
            
            plt.subplot(2,3,6)
            vr = np.diff(rs) / np.diff(time) * Rsun
            plt.plot(time[:-1],vr,'-o',color="black")
            plt.grid()
            plt.xlabel("Time [s]")
            plt.ylabel("Speed [km/s]")
            
            with open(paths[0]+'.table.txt', "w") as fp:   # Save x/y-data in file
                fp.write('    T[s],  F[MHz],   Ne[cm^-3], Rs[Rsun]\n') # write header information
                print '    T[s],  F[MHz],   Ne[cm^-3], Rs[Rsun]'
                for i in xrange(0,len(freq)):
                    st = '{:8.3f},'.format(time[i]) + \
                         '{:8.3f},'.format(freq[i]) + \
                        '{:12.1f},'.format(Ne[i])   + \
                          '{:5.2f}'.format(rs[i])
                    fp.write(st+'\n')      
                    print st

            print '\nStatistical results for CME velocity:'
            ym = np.mean(vr)
            st = 'Mean      ={:7.1f}'.format(ym) + ' km/s'
            print st
            
            ym = np.median(vr)
            st = 'Median    ={:7.1f}'.format(ym) + ' km/s'
            print st
    
            v1 = (rs[-1] - rs[0]) / (time[-1] - time[0]) * Rsun
            st = '1st order ={:7.1f}'.format(v1) + ' km/s'
            print st
            plt.savefig(paths[0]+'.results.png')


        else:    
            self.x = event.xdata
            self.y = event.ydata
            self.axes.plot(self.x, self.y, 'wo', linewidth = 10) #This don't work
            self.fig.canvas.draw_idle()
            #global coords
            coords.append((self.x, self.y)) # update x/y-array


mouse = MouseMonitor(fig, ax)

cid = fig.canvas.mpl_connect('button_press_event', mouse) 
#-----------------------------------------------------------------------------------------------
