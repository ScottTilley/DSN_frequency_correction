# DSN_frequency_correction

This simple juypter-notebook reads a time and range rate data file created by GMAT and applies Doppler correction to GQRX.

To make it work for you edit the following in the GMAT .script file and create a suitable .gmd file using GMAT2020:

1) Provide the suitable state vector:

Create Spacecraft Tianwen1;
Tianwen1.DateFormat = UTCGregorian;   
Tianwen1.Epoch = '01 Nov 2020 19:16:18.22';
Tianwen1.CoordinateSystem = SunICRF;
Tianwen1.DisplayStateType = Cartesian;
Tianwen1.X = 162176893.18858024
Tianwen1.Y = 89611204.03890982
Tianwen1.Z = 43297804.49442677
Tianwen1.VX = -8.556023611815943
Tianwen1.VY = 23.319737091646765
Tianwen1.VZ = 10.503682382842694
Tianwen1.AddHardware = {HGA, XBandTX};
Tianwen1.Id = '-9901491';

2) Update the following with your location info.  

VE7TIL.Location1 = 49.43479333333333;
VE7TIL.Location2 = 236.33117;
VE7TIL.Location3 = 0.04;

3) Update the time the filename for the .gmd file to be called.  It appears in the GMAT output directory.

VE7TILData.FileName = {'ve7til_2020_11_3.gmd'};

4) Update the start/stop time of your observing window:

Sim.InitialEpoch = '03 Nov 2020 00:00:00'; 
Sim.FinalEpoch = '03 Nov 2020 23:59:59'; 

5) You can do a find and replace for all the VE7TIL and replace with your call if you like but this won't change the operation.
