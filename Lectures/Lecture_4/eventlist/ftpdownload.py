# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 17:33:00 2018
Lecture 4.5/5 Download event-list from SWPC/NOAA FTP-server
@author: Hitsch
"""
import urllib
 
#-----------------------------------------------------------------
url = 'ftp://ftp.swpc.noaa.gov/pub/warehouse/2014/'
myfile = '2014_events.tar.gz'
myurl = url + myfile
print "Downloading Event-file with urllib from: " + myurl
urllib.urlcleanup()
urllib.urlretrieve(myurl, myfile)
#-----------------------------------------------------------------
