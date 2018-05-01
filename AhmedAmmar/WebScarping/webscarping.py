# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: Downlowad e-CALLISTO dat from web site
Inputs: url
Outputs:  .fit.gz files into local directory
Date Created: Mon Apr 30 19:00:18 2018
Date Modified: M D, Y
Date Released: M D, Y
Sources: 
    bs4: https://stackoverflow.com/questions/16368466/how-can-i-download-all-types-of-file-in-python-with-request-library
Versions:
    V0.01: ---
    
'''

#import urllib2 # for python 2
import urllib
from bs4 import BeautifulSoup

url = "http://soleil80.cs.technik.fhnw.ch/solarradio/data/2002-20yy_Callisto/2017/09/06/"

site = urllib.urlopen(url)
html = site.read()
soup = BeautifulSoup(html, "lxml")

list_urls = soup.find_all('a')

#print(list_urls[6])
#newurl = list_urls[2521]['href']
#print(newurl)
#print(len(list_urls))

for i in range(5, len(list_urls)-1):
    myfile = list_urls[i]['href']
    url2= url + myfile
#    myfile = url2.rsplit('/', 1)[1] # extract filename from URL
    print(myfile)
    urllib.urlretrieve(url2, myfile)