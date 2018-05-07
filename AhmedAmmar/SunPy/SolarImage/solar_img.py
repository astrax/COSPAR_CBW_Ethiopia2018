# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: 
Created on Thu May 03 15:44:07 2018
'''
import sunpy.map
from sunpy.net import helioviewer
import matplotlib.pyplot as plt
import sunpy.cm as cm

hv = helioviewer.HelioviewerClient()
data_sources = hv.get_data_sources()
filepath=hv.download_jp2('2012/07/03 14:30:00', observatory='SDO', instrument='AIA', detector='AIA', measurement='171', directory='.')
lascoC2 = sunpy.map.Map(filepath)

lascoC2.peek()
plt.show()