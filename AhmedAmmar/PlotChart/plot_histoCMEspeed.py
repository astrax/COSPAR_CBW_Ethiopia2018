# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:55:56 2018

@author: Ahmed
"""

import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------

plt.figure(figsize=(12,8))
myfile = "../events/MyBurstFile_TypeII_2017.txt"

with open(myfile, 'r') as infile:

    data = infile.read() 

my_list = data.splitlines()[1:]
#print my_list
vcme = []
#del vcme[:]
for line in my_list:
    st = line[-14:-10] # access velocity
#    print(st)
    try:
        y = float(st)
    except ValueError,e:
        print "error"
    vcme.append(y) # -> y-axis

bins = np.linspace(100, 1500, 10)  # -> x.axis

plt.hist(vcme, bins, alpha=0.5,color='b',histtype='stepfilled',linewidth=3.0)
#histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional
# alpha = transparency factor

plt.xlabel('CME velocity [km/s]: ',fontsize=15)
plt.ylabel('Occurence',fontsize=15)
plt.title('Histogram CME velocities',fontsize=15)
plt.tick_params(labelsize=14)
plt.tight_layout()
plt.savefig(myfile[10:-4]+".png")
plt.show()