# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 08:07:50UT 2017
Updated on 
Generates plot of a text file with two columns
Allows zooming in and out as well as saving a png
Hands-on 1/5
@author: Chr. Monstein
"""

import numpy as np
from matplotlib import pyplot as plt
import os
from Tkinter import Tk
from tkFileDialog import askopenfilename
#--------------------------------------------------------------------------------
Tk().withdraw() # 
myfile = askopenfilename() # show an "Open" dialog box and return file

f = open(myfile, 'r')
sky = np.genfromtxt(f, delimiter=',',skip_header=1)
x = sky[:,0]
y = sky[:,1]
f.close()
#--------------------------------------------------------------------------------
plt.figure()
plt.plot(x,y,'-o',color='green') #o,+,
fnam = os.path.basename(myfile) # extract filename only
plt.title(fnam,fontsize=16)
plt.text(70, 1300, 'FM',color="blue",size=20)


plt.show()

#--------------------------------------------------------------------------------

