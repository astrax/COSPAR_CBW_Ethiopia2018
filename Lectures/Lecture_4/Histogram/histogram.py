# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 16:33:38 2018
Lecture 4.4/5 Plot histogram of random number distributions

@author: Chr. Monstein
"""

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import random
import numpy
import matplotlib.pyplot as plt
#import plotly.plotly as py  # tools to communicate with Plotly's server
#-----------------------------------------------------------------------------

plt.figure(figsize=(12,8))

y1 = [random.gauss(4,1) for _ in range(400)]
y2 = [random.gauss(6,2) for _ in range(400)]

bins = numpy.linspace(0, 10, 50)  # -> x.axis

plt.hist(y1, bins, alpha=0.5,color='r',histtype='step',linewidth=3.0)
plt.hist(y2, bins, alpha=0.5,color='g')
#histtype : {‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}, optional
# alpha = transparency factor

plt.xlabel('Frequency driftrate [MHz/s] ',fontsize=15)
plt.ylabel('Number of type II bursts observed',fontsize=15)
plt.title('Two classes of driftrate of type II bursts',fontsize=15)
plt.tick_params(labelsize=14)
plt.grid(axis='both')
plt.savefig("MyHistogram.png")
plt.show()
#-----------------------------------------------------------------------------
