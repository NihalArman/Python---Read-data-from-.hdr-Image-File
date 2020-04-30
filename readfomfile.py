import matplotlib.pyplot as plt
import numpy
import tkinter
from tkinter import*


#Read Spectral Image
path = r'F:\PHD\UEF Thesis\image set\card photogrammetry\Green paper photogrametry spectral images set\409\capture'

#Read HDR Content
hdr_path = r'F:\PHD\UEF Thesis\image set\card photogrammetry\Green paper photogrametry spectral images set\409\capture\409.hdr'

SpectralSample = 0
SpectralBand = 0
SpectralLine = 0

def read_hdr(hdr_path):
    f=open(hdr_path, "r")
    filelines = f.readlines()

#     # This reads everything from hdr file
#     for fileline in filelines:
#         print(fileline)
# read_hdr(hdr_path)
    f.close()
    bands = ''
    for fileline in filelines:
        if 'samples' in fileline.lower():
            samples = int(fileline.replace('samples = ',''))
            #print("print sample: ", end ='')
            #print(samples)

            #saving the value globally
            global SpectralSample
            SpectralSample = samples
        if bands == '' and 'bands' in fileline.lower():
            bands = int(fileline.replace('bands = ',''))
            #print(bands)

            # saving the value globally
            global SpectralBand
            SpectralBand = bands
        if 'lines' in fileline.lower():
            lines = int(fileline.replace('lines = ',''))
            # saving the value globally
            global SpectralLine
            SpectralLine = lines

#run function
read_hdr(hdr_path)
#print
print("print spectral sample: ", end ='')
print(SpectralSample)

print("print spectral band: ", end ='')
print(SpectralBand)

print("print spectral lines: ", end ='')
print(SpectralLine)

#Read Waves
n = 0

f=open(hdr_path, "r")
filelines = f.readlines()
bands = ''
n1 = filelines.index('wavelength = {\n')+1
n2 = n1 + SpectralBand
#print(n1)
#print(n2)

waves = numpy.zeros(n2-n1,)
for i in range(n1,n2):
    waves[n] = float(filelines[i].replace(',\n', ''))
    n=n+1

#print waves

print('print waves = ')
for wave in waves:
    print(wave)






