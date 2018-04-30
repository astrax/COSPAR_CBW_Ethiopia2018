# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: - - - 
Inputs: - - -
Outputs:  - - -
Date Created: Mon Apr 30 19:00:18 2018
Date Modified: M D, Y
Date Released: M D, Y
Sources: https://stackoverflow.com/questions/16368466/how-can-i-download-all-types-of-file-in-python-with-request-library
Versions:
    V0.01: ---
    
'''

#import urllib2 # for python 2
import urllib.request
from bs4 import BeautifulSoup

url = "http://soleil80.cs.technik.fhnw.ch/solarradio/data/2002-20yy_Callisto/2017/09/06/"

site = urllib.request.urlopen(url)
html = site.read()
soup = BeautifulSoup(html)

list_urls = soup.find_all('a')

#print(list_urls[6])
#newurl = list_urls[2521]['href']
#print(newurl)
#print(len(list_urls))

for i in range(5, len(list_urls)-1):
    newurl = list_urls[i]['href']
    print(newurl)