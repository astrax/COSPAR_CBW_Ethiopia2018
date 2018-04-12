# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:33:38 2018

Hands-on 3/5: Produce a histogram out of CME-velocities of 2010
@author: Chr. Monstein
"""
#--------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------

plt.figure(figsize=(12,8))
myfile = 'MyBurstFile_TypeII_2010.txt'

with open(myfile, 'r') as infile:
    data = infile.read() 

my_list = data.splitlines() 

vcme = []
del vcme[:]
for line in my_list:
    st = line[96:105] # access velocity
    try:
        y = float(st)
    except ValueError,e:
        print "error"
    vcme.append(y) # -> y-axis

bins = np.linspace(100, 1500, 10)  # -> x.axis

plt.hist(vcme, bins, alpha=0.5,color='b',histtype='bar',linewidth=3.0)
#histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional
# alpha = transparency factor

plt.xlabel('CME velocity [km/s]: ',fontsize=15)
plt.ylabel('Occurence',fontsize=15)
plt.title('Histogram CME velocities',fontsize=15)
plt.tick_params(labelsize=14)

plt.show()
#--------------------------------------------------------------------------------
