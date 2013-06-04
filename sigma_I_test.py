# -*- coding: utf-8 -*-
"""
Created on Sun Jun 02 15:25:09 2013

@author: Will
"""

from CloudImage import CloudImage
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.constants import pi, hbar, alpha, c
from acmconstants import OMEGA_RES, LINEWIDTH_RES, G1, D12, G2
import logging

ms = 1e-3
um = 1e-6
mm = 1e-3
uW = 1e-6

test_image = CloudImage('test_image_recent.mat')
omega = OMEGA_RES

raw_atom_number = test_image.getAtomNumber()[0][0]
print 'Atom Number: %d'%raw_atom_number
print 'Magnification: %f'%test_image.magnification

test_image.truncate_image(400,1000, 0, 500) #empirical, image-specific


def gH(omega, omega_resonance, linewidth):
    '''Lineshape Function'''
    return (linewidth / (2*pi*((omega - omega_resonance)**2 
                                + 0.25*linewidth**2)))

def sigma(intensity_image, omega):
    '''intensity and frequency dependent cross section'''
    A21 = (G1*4*alpha*((omega)**3)*(D12**2)) / (G2*3*c**2)
#    print 'A21:'
#    print A21
    abs_x_section = ((3 * pi**2 * c**2 * A21 * 
                gH(omega, OMEGA_RES, LINEWIDTH_RES)) 
                / (OMEGA_RES**2))
    abs_x_section_0 = ((3 * pi**2 * c**2 * A21 * 
                gH(OMEGA_RES, OMEGA_RES, LINEWIDTH_RES)) 
                / (OMEGA_RES**2))
#    print 'lineshape factor:'
#    print gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES)
#    print 'x_section:'
#    print abs_x_section

    I_sat = (hbar*OMEGA_RES*A21)/(2*abs_x_section_0)
#    print "I_sat = %f"%I_sat
    
    return abs_x_section / (1 + intensity_image / I_sat)
    
def sigma_const(beam_intensity, omega):
    '''intensity and frequency dependent cross section'''
    A21 = (G1*4*alpha*((omega)**3)*(D12**2)) / (G2*3*c**2)
#    print 'A21:'
#    print A21
    abs_x_section = ((3 * pi**2 * c**2 * A21 * 
                gH(omega, OMEGA_RES, LINEWIDTH_RES)) 
                / (OMEGA_RES**2))
    abs_x_section_0 = ((3 * pi**2 * c**2 * A21 * 
                gH(OMEGA_RES, OMEGA_RES, LINEWIDTH_RES)) 
                / (OMEGA_RES**2))
#    print 'lineshape factor:'
#    print gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES)
#    print 'x_section:'
#    print abs_x_section

    I_sat = (hbar*OMEGA_RES*A21)/(2*abs_x_section_0)
#    print "I_sat = %f"%I_sat
    
    return abs_x_section / (1 + beam_intensity / I_sat)
    
def get_I_sat(omega):
    '''intensity and frequency dependent cross section'''
    A21 = (G1*4*alpha*((omega)**3)*(D12**2)) / (G2*3*c**2)
#    print 'A21:'
#    print A21
    abs_x_section_0 = ((3 * pi**2 * c**2 * A21 * 
                gH(OMEGA_RES, OMEGA_RES, LINEWIDTH_RES)) 
                / (OMEGA_RES**2))
#    print 'lineshape factor:'
#    print gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES)
#    print 'x_section:'
#    print abs_x_section

    I_sat = (hbar*OMEGA_RES*A21)/(2*abs_x_section_0)
#    print "I_sat = %f"%I_sat
    
    return I_sat

def gaussian1D(x,A,mu,sigma,offset):
    return A*np.exp(-1.*(x-mu)**2./(2.*sigma**2.)) + offset

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return [array[idx],idx]

def fitGaussian1D(image, xdata = []): #fits a 1D Gaussian to a 1D image
    # from Matt's CloudImage class
    if xdata == []:
        xdata = np.arange(np.size(image))
    max_value = image.max()
    max_loc = xdata[np.argmax(image)]
    [half_max,half_max_ind] = find_nearest(image,max_value/2.)
    hwhm = abs(xdata[half_max_ind] - max_loc)
    p_0 = [max_value,max_loc,hwhm,0.] #fit guess
#    xdata = np.arange(np.size(image))
    
    coef, outmat = curve_fit(gaussian1D,xdata,image,p0 = p_0)
    return coef

#coef = fitGaussian1D(np.nansum(test_image.lightImage, 0))
#
### Unused code for plotting before changing to physical quantities
##plt.plot(np.nansum(test_image.lightImage, 0))
##x_camera = xrange(0, test_image.lightImage.shape[0])
##plt.plot(gaussian1D(x_camera, coef[0], coef[1], coef[2], coef[3]))
##plt.show()
#
#print '''
#         A:      %.0f
#         mu:     %.0f
#         sigma:  %.0f
#         offset: %.0f'''%(coef[0], coef[1], coef[2], coef[3])

QE = 0.20 #rough value from datasheet curve
exp_time = 0.2*ms
#exp_time = 10*ms
pixel_size = 3.75*um
camera_gain = 16
M = test_image.magnification[0][0]
real_pixel_area = (pixel_size / M)**2
print "Real Pixel Area (um^2): %f"%(real_pixel_area / um**2)
#omega = OMEGA_RES
intensityImage = ((hbar * omega) / (QE * exp_time * real_pixel_area * camera_gain)) * test_image.lightImage_trunc
print "hbar: %e"%hbar

#print pixel_size / M
#image_size = test_image.lightImage.shape[1]*pixel_size / M
n_pixels = intensityImage.shape[1]
image_size = n_pixels * pixel_size / M

logging.debug('n_pixels: %d'%n_pixels)
logging.debug('n_pixels_image: %d'%len( np.nansum(intensityImage, 0)))

x_true = np.linspace(0, image_size,n_pixels)

logging.debug('x_true: %s'%x_true)
logging.debug('image size: %f'%max(x_true))
logging.debug('x_size: %d'%len(x_true))

plt.plot(x_true, np.nansum(intensityImage, 0))
coef = fitGaussian1D(np.nansum(intensityImage, 0), x_true)
plt.plot(x_true, gaussian1D(x_true, coef[0], coef[1], coef[2], coef[3]))
#plt.show()

w_z = (2. * coef[2])
I_0z = (pixel_size / M) * coef[0] / (coef[2] * (2 * pi)**-0.5)
power = 0.5 * pi * I_0z * w_z**2

print '''
         I_0z:       %e
         w_z (mm):   %2.2f
         power(uW):  %2.2f
         I/I_sat :   %2.2f\n'''%(I_0z, w_z / mm, power / uW, I_0z / get_I_sat(omega))
         
#print np.nanmax(intensityImage)
#print np.nanmax(sum(intensityImage, 0))
#print coef[2] * pixel_size / M
#print np.sum(intensityImage)
print np.sum(intensityImage) * ((pixel_size / M)**2)
print power / 15.4e-6
print 15.4e-6 / power
#print test_image.A[0][0]
#print np.nanmax(sigma(intensityImage, omega))
#print test_image.s_lambda[0][0]
#im = plt.plot(sigma(intensityImage, omega)[100])
#plt.show()
#im2 = plt.imshow(test_image.getODImage())
#plt.show()
#im3 = plt.plot(test_image.getODImage()[100])
#plt.show()

def getAtomNumber(image_set, omega):
    ODImage = image_set.getODImage()
    atomNumber = image_set.A * np.sum(ODImage / sigma(intensityImage, omega));
    return atomNumber
    
def getAtomNumber_const(image_set, omega):
    ODImage = image_set.getODImage()
    atomNumber = image_set.A * np.sum(ODImage / sigma_const(I_0z, omega));
    return atomNumber
    
sat_corrected_number = getAtomNumber(test_image, omega)[0][0]
print sat_corrected_number / raw_atom_number
const_sigma_corrected_num = getAtomNumber_const(test_image, omega)[0][0]
print 'intensity variation correction: %2.5f'%((sat_corrected_number - const_sigma_corrected_num) / sat_corrected_number)

#for line in test_image.runDataFiles[0,0]:
#    if line:
#        print line[0]
#print test_image.runDataFiles[0,0][10][14][0]

#
#for file in test_image.runDataFiles[0,0][10]:
#    if file[0] == u'Variables.m':
#        variables =  iter(file[1][0].split('\n'))
#        for value in variables:
#            if value == 'ExposeTime':
#                print value
#                print variables.next()
#                print variables.next()
#            print value