# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: Downlowad e-CALLISTO dat from web site
Inputs: url
Outputs:  .fit.gz files into local directory
Date Created: Mon Apr 30 19:00:18 2018
Help sources: 
    1) bs4: https://stackoverflow.com/questions/16368466/how-can-i-download-all-types-of-file-in-python-with-request-library
'''

#import urllib2 # for python 2
import os
import urllib
from bs4 import BeautifulSoup

year = "2017"
month = "09"
day ="06"
url = "http://soleil80.cs.technik.fhnw.ch/solarradio/data/2002-20yy_Callisto/" + year + "/" + month + "/" + day + "/"

#dist_dir="H:\\COSPAR_DATA\\CALLISTO\\2017\\09\\04\\" # external hard disc
data_dir= "..\\DataCALLISTO\\"
if not os.path.isdir(data_dir + year + "\\"):
    os.mkdir(data_dir + year + "\\")
if not os.path.isdir(data_dir + year + "\\" + month + "\\"):
    os.mkdir(data_dir + year + "\\" + month + "\\")
if not os.path.isdir(data_dir + year + "\\" + month + "\\" + day + "\\"):
    os.mkdir(data_dir + year + "\\" + month + "\\" + day + "\\")
    
dist_dir= "..\\DataCALLISTO\\" + year + "\\"+ month + "\\" + day + "\\" # local 
site = urllib.urlopen(url)
html = site.read()
soup = BeautifulSoup(html, "lxml")

list_urls = soup.find_all('a')

#print(list_urls[6])
#newurl = list_urls[2521]['href']
#print(newurl)
#print(len(list_urls))
print("----------------------------\nDownloading data \n----------------------------\n")

for i in range(5, len(list_urls)-1):
    myfile = list_urls[i]['href']
    url2= url + myfile
    myfile = url2.rsplit('/', 1)[1] # extract filename from URL
    # StationName = myfile[:-26]
    if myfile[:-26]=='GREENLAND' and 11<= int(myfile[-16:-14])<=13:
        print(myfile)
        #Save files in directory
        urllib.urlretrieve(url2, dist_dir+myfile)
    
print("----------------------------\nDone! \n----------------------------")