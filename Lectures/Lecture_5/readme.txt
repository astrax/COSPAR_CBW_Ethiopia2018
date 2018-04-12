Lecture 5

5.1 Read FIT-file from GOES and plot light curve(s), study and print header information -> Folder GOESlightcurve, script goes.py
    Change x-axis from seconds into hours 0..24

5. Fit the leading edge of a light curve from GOES with different methods
5.2 Gauss' approximation (add labels and title)  -> CurevFitting->fitgoes2.py add a title to the 2nd plot
    amp/(np.sqrt(2*np.pi)*wid)) * np.exp(-(x-cen)**2 /(2*wid**2)

5.3 Exponential function (add labels and title)  -> CurevFitting->fitgoes3.py add a title to the 2nd plot
    coeffs[0] + coeffs[1] * np.exp( - ((t-coeffs[2])/coeffs[3])**2 )

5.4 Polynomial with 3 coefficients               -> CurevFitting->fitgoes4.py add a title to the 2nd plot
    coeffs[0] + coeffs[1] * 1./(t-coeffs[2])

5.5 Polynomial with 5 coefficients               -> CurevFitting->fitgoes5.py 
    coeffs[0] + coeffs[1] * (t-coeffs[4]) + coeffs[2] * (t-coeffs[4])**2 + coeffs[3] * (t-coeffs[4])**3

5.6 nonlinear fit (log)                          -> CurevFitting->fitgoes6.py
    coeffs[0]/(((t-coeffs[1])/coeffs[2]))**(1.+np.log((t-coeffs[1])/coeffs[2]))

5.7 Non linear fit of a table                    -> CurevFitting->nonlinearfit.py add x-axis label, y-axis label and a title
    a * x / (b + x)


 Image manipulation
5.8 resize an image such that it can be merged with another one -> Folder ImageManipulation, script imgresize.py
5.9a merge different spectra in a horizontal mode               -> Folder ImageManipulation, script imgstack.py
5.9b merge different spectra in a vertical mode                 -> Folder ImageManipulation, script imgstack.py
5.9c merge GOES-light curve with type II burst spectrum         -> Folder ImageManipulation, script imgstack.py
