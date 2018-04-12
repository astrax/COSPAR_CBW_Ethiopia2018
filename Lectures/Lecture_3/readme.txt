Lecture 3

- 3.1 plot a single spectrum in dB out of a 2-dimensional FIT-file at a dedicated time-event -> Folder SingleSpectrum, script plotSingleSpec.py
      Play with selection of different time-slots in lines 40-41
      Remember pseudo-calibration [dB] in line 45
      See, how time in the titel is printed!

- 3.2 plot a single light curve in dB out of a 2-dimensional FIT-file at a dedicated frequency -> Folder Lightcurve, script plotLightcurve.py
      Use Javaviewer to identify frequency of interest. By printing freqs[a number 0...199] find corresponding channel-number
      Do this for frequency of interest and put the number in line 40
      In line 45 the lowest value found of the light-curve will be subtracted in line 46 including pseudo-calibration in dB
      Play also with smoothing value in line 44

- 3.3 swap frequency-axis and save in different graphic formats -> Folder AxisFlip, script FITplotAxisFlip.py
      Some scientists want to have lowest frequency at the top because axis could then replaced by solar radius. 
      Others want to have lowest frequency at the bottom as usual in xy-plots (individual preferences).
      Play with clip-values in line 30 as well as with color-map in lines 34 and 48
      Which version do you prefer?
      See also on how to save eps figures, mostly used in publications.
      

