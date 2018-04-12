# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:45:21 2018
Lecture 4.3/5 Plot bar-chart

@author: Christian Monstein


In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
#-----------------------------------------------------------------------------

import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels  = 'Frogs', 'Hogs', 'Dogs', 'Crocodiles'
sizes   = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.figure(figsize=(7,7))
plt.rcParams['text.color'] = 'black'
plt.title('Raining Hogs and Dogs')

plt.rcParams['font.size'] = 19.0
plt.rcParams['text.color'] = 'mediumblue'

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',shadow=True, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("MyPieChart.png")
plt.show()
#-----------------------------------------------------------------------------
