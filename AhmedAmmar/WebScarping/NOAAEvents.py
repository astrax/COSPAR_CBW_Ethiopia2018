# -*- coding: utf-8 -*-
"""
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: NOAA solar events from FTP server
Inputs: url
Outputs:  
Created on Thu May 10 10:50:14 2018

"""
import os
import urllib
import tarfile
import glob

dist_dir= "../events/" # local 

def DownloadEvents(start_year=2010, end_year=2017):
    '''
    Downoad NOAA solar events from FTP server:
        1. Download .tar.gz files.
        2. Extract events files.
        3. Delete .tar.gz files
    '''
    yearList= range(start_year,end_year+1)
    
    for year in yearList:
        # Download .tar.gz files
        url = 'ftp://ftp.swpc.noaa.gov/pub/warehouse/' + str(year) + '/'
        myfile = str(year) + '_events.tar.gz'
        myurl = url + myfile
        print "Downloading Event-file with urllib from: " + myurl
        urllib.urlcleanup()
        urllib.urlretrieve(myurl, dist_dir + myfile)
        # Extract files
        tar = tarfile.open(dist_dir + myfile, "r:gz")
        #print tar.getnames()
        for member in tar.getmembers():
            print "Extracting %s" % member.name
            tar.extract(member, path= dist_dir)
        tar.close()
        
        # Delete '*_events.tar.gz' files"
        file2rmv= dist_dir+ myfile
        if os.path.isfile(file2rmv):
            os.remove(file2rmv)
            
def BurstFinder(myYear= "2010", BurstType= 2):
    '''
    Find Radio Burst events and save them in text file:
        - Save burst II events for one year.
    Param:
        - myYear = str
        - BurstType = 1....6
    '''
    bursttypes = [' I/',' II/',' III/',' IV/',' V/',' CTM']
    burstnames = ['TypeI','TypeII','TypeIII','TypeIV','TypeV','TypeCTM']
    liste = glob.glob(dist_dir + myYear+"_events/*.txt")
    liste.sort()
    
    outF = open(dist_dir + "MyBurstFile_" + burstnames[BurstType-1] + "_" + myYear + ".txt", "w")
    title = ' #Event    Begin    Max       End  Obs  Q  Type  Loc/Frq   Particulars       Reg#'
    print liste[0], title
    outF.write(liste[0] + ' '  + title)
    outF.write('\n')
    
    for day in liste:
        f = open(day, 'r')
        for line in f:
            if bursttypes[BurstType-1] not in (line): 
                continue 
            text = day + '->' + line
            print text,
            outF.write(text)
        f.close()
    outF.close()
def BurstGroup():
    '''
    Save burst II events for long period (more than one year)
    '''
    liste = glob.glob(dist_dir + "*.txt")
    liste.sort() 
    outF = open(dist_dir + "MyBurstFile_TypeII_" + "2010-2017" + ".txt", "w")
    header = '#Day Event    Begin    Max       End  Obs  Q  Type  Loc/Frq   Particulars       Reg# \n'
    outF.write(header)
    for year in liste:
        f = open(year, 'r')
        lines = f.readlines()[1:]
        for line in lines:
            outF.write(line)
        f.close()
    outF.close()
            
if __name__ == "__main__":
#    DownloadEvents()
#    BurstFinder(myYear= "2017")
    BurstGroup()
    print("\nDone!")
