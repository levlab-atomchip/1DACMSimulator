# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:31:44 2013

Implementation assumes that an equal integer number of points lie on each pixel

@author: Will
"""
import AtomImage
import numpy as np
from Window import window
#from math import floor
from acmconstants import HBAR, OMEGA_RES, BG_NOISE_CURRENT

class CCD():
    def __init__(self, num_pixel, pixel_size, nbits, dark_current):
        self.num_pixel = num_pixel
        self.pixel_size = pixel_size
        self.nbits = nbits
        self.dark_current = dark_current
        self.length = num_pixel * pixel_size
        
    def image(self, analog_image, exposure_time):
        ''' produce a DigitalImage from an AtomImage '''

        image_res = (window.max - window.min) / window.num_cells #m
        pts_per_pix = int(self.pixel_size / image_res)

        signal = analog_image.get_image_arr()
        digital_image = []
        for i in range(self.num_pixel):
            binsum = sum(signal[(pts_per_pix*i):(pts_per_pix*(i+1))])
#            print binsum
            n_photons = (round(exposure_time * binsum * self.pixel_size**2 
                        / (HBAR * OMEGA_RES)) 
            + np.random.poisson(self.dark_current*exposure_time)
            + np.random.poisson(BG_NOISE_CURRENT * exposure_time))
#            digital_image.extend([binsum/pts_per_pix]*(pts_per_pix))
            digital_image.append(n_photons)
#            digital_image.append(binsum)
        
        output_image_arr = np.array(digital_image)
#        print 'output image:'
#        print output_image
#        print len(output_image)
        
#        output_image =atom_image.image #placeholder
        digital_image = AtomImage.DigitalImage(output_image_arr, self)
        return digital_image