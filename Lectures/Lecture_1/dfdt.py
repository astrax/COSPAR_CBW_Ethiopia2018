# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:35:36 2017
Lecture 1.3/5 Plot a mathematical function
@author: Christian
"""
from matplotlib import pyplot as plt
import numpy as np

#--------------------------------------------------------------------------------

plt.figure(figsize=(10,7))
fp = np.arange(10, 200, 2)
dfdt = 4.0e-4 * fp**1.27
plt.plot(fp,dfdt,'-sb')
plt.xlabel("Plasma frequency [MHz]",size=18)
plt.ylabel("df/dt [MHz/s]",size=18)
plt.title("Type II statistical drift rate", size=18)
plt.grid(True)
#plt.xscale('log')
#plt.yscale('log')
plt.tick_params(labelsize=20)
plt.plot(33.35,0.08,'-sr')  # measured driftrate MHz/s
plt.plot(31.9,0.065,'-sg')  # measured driftrate MHz/s
plt.plot(24.9,0.071,'-sm')  # measured driftrate MHz/s

plt.savefig("Driftrate.png")
plt.savefig("Driftrate.pdf")
plt.savefig("Driftrate.eps")
plt.savefig("Driftrate.tif")
#--------------------------------------------------------------------------------
