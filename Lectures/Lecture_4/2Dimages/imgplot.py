# -*- coding: utf-8 -*-
"""
Created on Tuesday, 2018-02-06
Lecture 4.1/5 How to plot 2-d images
@author: cmonstei
"""

from pylab import imread

import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------

imgfile = '2018_Ethiopia_meeting_logo_v3_yellow.jpg'
#imgfile = 'iswi_log.gif'
#imgfile = '1200px-NASA_logo.svg.png'
#imgfile = 'X17c3m.bmp'
#imgfile = 'typeII.tif'

image = imread(imgfile) 

plt.imshow(image)
plt.xlabel('x-axis pixel')
plt.ylabel('y-axis pixel')
plt.title('How to plot 2D-images')

plt.savefig('converted_'+imgfile+'.pdf')
plt.show()
#-----------------------------------------------------------------------------
