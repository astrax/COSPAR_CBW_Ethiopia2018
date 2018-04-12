# -*- coding: utf-8 -*-
"""
Created on Wed Feb 07 10:49:25 2018
pip install python-resize-image
Lecture 5.8/5 Image overlay, resizing an image for next script
@author: cmonstei
"""
#-------------------------------------------------------------------------------------------

from PIL import Image
#-------------------------------------------------------------------------------------------

basewidth = 800
img = Image.open('Ooty_TypeII.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('Ooty_TypeII_resized.jpg') 
#-------------------------------------------------------------------------------------------
