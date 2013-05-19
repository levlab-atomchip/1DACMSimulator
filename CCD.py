# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:31:44 2013

@author: Will
"""
import DigitalImage
import numpy as np

class CCD:
    def __init__(self, imaging_file):
        pass
#        self.resolution = resolution
#        self.nbits = nbits
        
    def image(self, atom_image):
        ''' produce a DigitalImage from an AtomImage '''
        output_image = np.zeros(atom_image.shape)
        digital_image = DigitalImage.DigitalImage(output_image, self)
        return digital_image