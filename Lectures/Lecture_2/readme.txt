Lesson 2

a) files access 3 different methods
- 2.1 save FIT-file(s) in the local folder, the same as the location of the Python script -> localaccess.py
      play with  color-table, fontsize, check other FIT-files from the archive
- 2.2 save FIT-file(s) in a separate local folder, not the same as the Python script -> sepaccess.py
      Do not forget to adjust your path-description. Download another FIT-file and play with image-size and color-map
- 2.3 access FIT-file(s) directly from website at central server -> webaccess.py
      Try another FIT-file from the archive, e.g. from Kazakhstan.

b) background subtraction methods (Folder: BackgroundSubtraction)
- 2.4 subtract constant value -> Folder constantvalue, script constant.py
      Play with vmin and vmax as well as with color-map. Which one looks best?
      
- 2.5 subtract average spectrum -> Folder specaverage, script average.py
      Do not forget to adjust your path-description.
      Play again with vmin and vmax as well as with color-map. Which one looks best?
      
      
- 2.6 subtract an individual spectrum -> Folder specindividual, script individual.py
      Play with pixelnumber of the reference spectrum (timemarker). Try several other
      spectra for subtraction between 0 and 3599. Which one looks best?

c) 2.7 Merge different spectra in frequency space -> Folder MergeFrequencySpace, script mergefrequency.py
       Use JavaViewer to identify frequency-limits for merging.
       print frequency[number] to find out limits, e.g freqs1[178] and freqs2[182] in console window
       ! we need to create a new frequency axis, see lines 48...50

   2.8 Improve axis-labels, colour tables, filtering -> Folder axis, script FITplotWithAxes.py
       Play with fmin, fmax, tmin, tmax for zooming. Play with clip-function in line 46
       as well as with vmin and vmax in line 65-66 and in lines 111-112
       Which of these 3 plots looks best and why? Wich one is your preferred one?
        
   2.9a Pseudo calibration of bursts in dB with color bar -> Folder pseudocal, script pseudocal.py (white background)
        Play with vmin, vmax in line 47 as well as with color-map
        See pseudo-calibration code in lines 42-45

   2.9b Pseudo calibration of bursts in dB with color bar -> pseudocal_BBG.py (black background)
        Play with vmin, vmax in line 47 as well as with color-map
        See pseudo-calibration code in lines 42-45
        Also play with background subtraction method in line 34 (1=single spectrum subtraction, 0=average spectrum subtraction)

   2.10 Use of extra library SunPy -> Folder SunPy, script SolarBurst_Example03.py
        Easy to use, but difficult to change things.
        Play with x-axis-limits (expressed in pixels)
        Play with vmin to adjust background
        Play with plt.figure(figsize=(width, height))
        Play with tools on top of the image-window (move, zoom, edit, save, ....)
