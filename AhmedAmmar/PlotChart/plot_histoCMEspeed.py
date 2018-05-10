# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:55:56 2018

@author: Ahmed
"""

import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------

#plt.figure(figsize=(12,8))
myfile = "../events/MyBurstFile_TypeII_2010-2017.txt"

vcme=np.loadtxt(myfile, comments='#', delimiter=' ', skiprows=0, usecols=15, unpack=True)
print vcme

#bins = np.linspace(100, 1500, 10)  # -> x.axis
#
#plt.hist(vcme, bins, alpha=0.5,color='b',histtype='bar',linewidth=3.0)
##histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional
## alpha = transparency factor
#
#plt.xlabel('CME velocity [km/s]: ',fontsize=15)
#plt.ylabel('Occurence',fontsize=15)
#plt.title('Histogram CME velocities',fontsize=15)
#plt.tick_params(labelsize=14)
#plt.tight_layout()
#plt.savefig(myfile+".png")
#plt.show()