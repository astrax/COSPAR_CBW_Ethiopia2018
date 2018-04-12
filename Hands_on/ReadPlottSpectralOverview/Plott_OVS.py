# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 08:07:50UT 2017
Updated on 
Generates plot of spectral overview file (csv and prn) from Callisto
Allows zooming in and out as well as saving a png

@author: Chr. Monstein
"""
db = False  # True or False
import numpy as np
from matplotlib import pyplot as plt
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
#--------------------------------------------------------------------------------
Tk().withdraw() # 
myfile = askopenfilename() # show an "Open" dialog box and return file

f = open(myfile, 'r')
sky = np.genfromtxt(f, delimiter=';',skip_header=1)
if (db):
    y   = (sky[:,1]-np.min(sky[:,1]))/2500.0*25.4
else:
    y = sky[:,1]
f.close()
freq = sky[:,0]
#--------------------------------------------------------------------------------
plt.figure()# present raw data from spectral verview
plt.plot(freq,y,'-',color="green") #o,+,
plt.xlabel("Frequency [MHz]",fontsize=15)
plt.ylabel("Intensity [mV]",fontsize=15)
fnam = os.path.basename(myfile) # extract filename only
plt.title(fnam,fontsize=16)
plt.text(70, 1300, 'FM',color="blue",size=20)
plt.tick_params(labelsize=14)
plt.grid()
plt.tight_layout()
plt.show()
plt.savefig(myfile+'_raw.png')
#--------------------------------------------------------------------------------

