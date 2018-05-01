# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: - - - 
Inputs: - - -
Outputs:  - - -
Date Created: Fri Apr 27 19:48:44 2018
Date Modified: M D, Y
Date Released: M D, Y
Versions:
    V0.01: ---
    
'''

from guiqwt.plot import ImageDialog
from guiqwt.tools import PointTool, AnnotatedPoint
from guiqwt.styles import AnnotationParam
import guidata
from guiqwt.builder import make
import pyfits
import numpy as np

def fun(shape):
    shape.symbol.pen().setWidth(5)
    shape.symbol.setColor(guidata.qt.QtGui.QColor(255,0,0))
    x=shape.get_pos()
    print(x)


myfile = 'BIR_20110809_080000_59.fit.gz'

hdu   = pyfits.open(myfile)
data  = hdu[0].data.astype(np.float32)
freqs = hdu[1].data['Frequency'][0] # extract frequency axis
time  = hdu[1].data['Time'][0] # extract time axis
hdu.close()
    
_app = guidata.qapplication()
win = ImageDialog(toolbar=True)
win.add_tool(PointTool, handle_final_shape_cb=fun)

#filename = osp.join(osp.dirname(__file__), "GAURI_20110809_075959_59.fit.gz.png")
#image = make.image(filename=filename, colormap="bone")
print(np.shape(data))
image = make.xyimage(time,freqs,data,colormap='gray')

plot = win.get_plot()
plot.add_item(image)

win.exec_()