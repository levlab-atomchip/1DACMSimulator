# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:28:59 2013

@author: RTurner
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import random
import scipy.fftpack as fftpack

random.seed()

PIXELSIZE = 10e-6 #m
IMAGERES = 1e-7 #m
PTSPERPIX = int(PIXELSIZE/IMAGERES)
CCDSIZE = 1024 #pixels

def CCDbin(signal):
    digital_image = []
    for i in range(CCDSIZE):
        binsum = sum(signal[(PTSPERPIX*i):(PTSPERPIX*(i+1))])
        digital_image.extend([binsum/PTSPERPIX]*(PTSPERPIX))
    digital_image.append(0)
    return digital_image
    
def CCDsample(signal):
    sampled_image = []
    for i in range(CCDSIZE):
#        sampled_image.append(signal[PTSPERPIX*i])
        sampled_image.extend([signal[PTSPERPIX*i]]*(PTSPERPIX))
    sampled_image.append(0)
    return sampled_image
    
lambdas = np.logspace(-7,-4, num = 300)
xaxis = np.arange(0,PIXELSIZE*CCDSIZE, IMAGERES)
CCDxaxis = range(CCDSIZE)
#print len(CCDxaxis)

bin_gains = []
sample_gains= []

for wavelength in lambdas:
    phase = random.uniform(0,2*math.pi)
#    phase = 0
    modulation = [(math.sin(2*math.pi*(x - phase)/wavelength)) for x in xaxis]
    
    modfft = fftpack.fftshift(fftpack.fft(modulation))
    modpwr = [abs(z) for z in modfft]
#    plt.semilogy(fftpack.fftfreq(len(modulation)), modpwr)
#    plt.show()
    
    signal = [y for y in modulation]
    digital_image = CCDbin(signal)
    sampled_image = CCDsample(signal)
#    print len(modulation)
#    print len(digital_image)
#    print digital_image
#    print digital_image[1:100]
#    digital_amplitude = max(digital_image) - min(digital_image)
#    sampled_amplitude = max(sampled_image) - min(sampled_image)
#    digital_amplitude = np.std(digital_image)
    bin_amplitude = sum([modulation[i]*digital_image[i] for i in range(len(modulation))])
    
    binfft = fftpack.fftshift(fftpack.fft(digital_image))
    binpwr = [abs(z) for z in binfft]
#    plt.semilogy(fftpack.fftshift(fftpack.fftfreq(len(digital_image))),binpwr)
#    plt.show()    
    
#    sampled_amplitude = np.std(sampled_image)
    sampled_amplitude = sum([modulation[i]*sampled_image[i] for i in range(len(modulation))])
#    sampled_amplitude = sum([i * j for i in modulation for j in sampled_image])
    bin_gains.append(abs(bin_amplitude))
    sample_gains.append(abs(sampled_amplitude))
#    plt.plot(xaxis, digital_image)
#    plt.plot(xaxis, modulation)
#    plt.plot(CCDxaxis, sampled_image)
#    plt.ylim((-2,2))
#    plt.show()
print "Gains Calculated"
    
plt.semilogx(lambdas, bin_gains)
plt.semilogx(lambdas, sample_gains)
plt.show()
    

    

#plot gain