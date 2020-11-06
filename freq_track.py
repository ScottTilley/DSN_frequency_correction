# DSN Doppler frequency correction for GQRX
# Requires GMAT generated .gmd file with time and rangerate data
# Scott Tilley, VE7TIL 

import telnetlib
import numpy as np
import time
from astropy.time import Time
from scipy.constants import c
from datetime import datetime

HOST = "localhost"
PORT = "7356"

tn = telnetlib.Telnet(HOST, PORT)

f_carrier = 8431016530.542998 # nominal carrier freqeuncy of TIANWEN-1

def writeCommand(cmd):
    tn.write(('%s\n' % cmd).encode('ascii'))
    return tn.read_some().decode('ascii').strip();

def writeFreq(freq):
    writeCommand("F " + str(freq))

gmd_file = '/home/scott/code/GMAT/R2020a/output/ve7til_2020_11_6.gmd' #uses state vector 2020-10-30T03:43:22.9642
gmd_mjd = []
gmd_rangerate = []
with open(gmd_file) as f:
    for l in f.readlines()[2:]:
        gmd_mjd.append(float(l.split()[0]))
        gmd_rangerate.append(float(l.split()[-1]))
gmd_mjd = np.array(gmd_mjd)
gmd_rangerate = np.array(gmd_rangerate)
t_gmd = Time(gmd_mjd + (2430000.0 - 2400000.5), scale = 'tai', format = 'mjd')

t_data = Time(Time.now(), scale = 'tai', format = 'mjd')
i = 0  

#Find initial index
while t_data > t_gmd[i]:
    i = i + 1
    
freq_last = f_carrier * (1 - 1e3*gmd_rangerate[i]/c)    
writeFreq(freq_last)

#loop forever and only update freqeuncy when a change is required based on rangerate data    
while True:
    t_data = Time(Time.now(), scale = 'tai', format = 'mjd')
       
    while  t_data > t_gmd[i]:  
        freq = f_carrier * (1 - 1e3*gmd_rangerate[i]/c)
        
        if int(freq) != int(freq_last):
            writeFreq(freq)
            freq_last = freq
        i = i + 1
        print("Index {:5d} /".format(i),"{:5d}".format(len(t_gmd)), "- Frequency {:10.4f}".format(freq), end="\r")
    time.sleep(0.1)
