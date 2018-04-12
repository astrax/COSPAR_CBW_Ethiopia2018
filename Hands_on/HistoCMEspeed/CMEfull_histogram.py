# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:33:38 2018

Hands-on: Produce a histogram out of CME-velocities 2010-2017
@author: Chr. Monstein
"""
#--------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------

vcme = []
del vcme[:]
my_list = []

myfiles = ['MyBurstFile_TypeII_2010.txt','MyBurstFile_TypeII_2011.txt','MyBurstFile_TypeII_2012.txt',
           'MyBurstFile_TypeII_2013.txt','MyBurstFile_TypeII_2014.txt','MyBurstFile_TypeII_2015.txt',
           'MyBurstFile_TypeII_2016.txt','MyBurstFile_TypeII_2017.txt']
#--------------------------------------------------------------------------------
        
plt.figure(figsize=(10,6))

data = []
for myfile in myfiles:
    with open(myfile, 'r') as infile:
        data = infile.read()   # large memory with data 
        Dy = data.splitlines() # here we separate data by comma

    my_list = my_list + Dy  # concatenate list per year to a full list
    
y = 0
for myline in my_list:
    st = myline[96:105] # grab CME velocity column out of the text-line
    try:
        y = float(st)
    except ValueError,e:
        errormessage = "Error: empty line or non-float value!"
        #print "error ",st
    vcme.append(y) # -> y-axis

bins = np.linspace(100, 1500, 14)  # -> generate x.axis

plt.hist(vcme, bins, cumulative=False,alpha=0.5,color='g',histtype='barstacked',linewidth=1.0)
#histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional
# alpha = transparency factor

plt.xlabel('CME velocity [km/s]: ',fontsize=15)
plt.ylabel('Occurence',fontsize=15)
plt.title('Distribution of CME velocities 2010-2017',fontsize=15)
plt.tick_params(labelsize=14)
#plt.grid(axis='both')
#plt.xscale('log')
plt.savefig("MyFull_Histogram.png")
plt.show()
#--------------------------------------------------------------------------------
