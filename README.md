# DSN_frequency_correction

This simple juypter-notebook reads a time and range rate data file created by GMAT and applies Doppler correction to GQRX.

To make it work for you edit the following in the GMAT .script file and create a suitable .gmd file using GMAT2020:

1) Provide the suitable state vector for spacecraft of interest.

2) Update with your location info.  

3) Update the filename for the .gmd file to be called.  It appears in the GMAT output directory.

4) Update the start/stop time of your observing window:

5) You can do a find and replace for all the VE7TIL and replace with your call if you like but this won't change the operation.
