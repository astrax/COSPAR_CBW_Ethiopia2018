# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:51:29 2017
Use a python console (not an ipython)
mouse click saves x-/y-coords of an image or plot
left mouse event.buttion == 1 -> save coorinates
right mouse event.button == 3 -> close file and exit
wheel/thumb event.buttion = 2
Hands-on 2/5
@author: cmonstei
"""
#--------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pyfits
import matplotlib.pyplot as mpl
from matplotlib import cm

#--------------------------------------------------------------------------------
files = 'OOTY_20100613_053001_58.fit.gz'
mpl.rcParams['font.size'] = 16

fds = pyfits.open(files)
data = fds[0].data

fig, ax = plt.subplots(1)
ax.imshow(data, aspect = 'auto',cmap=cm.plasma_r) # jet, CMRmap, gnuplot2, magma, plasma

ax.autoscale = False

class MouseMonitor:
    flag = True
    x = 0.
    y = 0.  
    fig = None
    axes = None

    def __init__(self, fig, ax):
        self.axes = ax
        self.fig = fig
    def __call__(self, event):
        if (event.button==1):
            self.x = event.xdata
            self.y = event.ydata
            self.axes.plot(self.x, self.y, 'w+', linewidth = 5) #This don't work
            self.fig.canvas.draw_idle()
        if (event.button==3):
            print 'Exit'

mouse = MouseMonitor(fig, ax)

cid = fig.canvas.mpl_connect('button_press_event', mouse) #--------------------------------------------------------------------------------