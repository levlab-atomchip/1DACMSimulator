# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:29:28 2013

@author: Will
"""

class AtomImage:
    ''' 1D array of light intensity after imaging '''
    def __init__(self, intensity_array, imaging_beam):
        self.image = intensity_array
        self.imaging_beam = imaging_beam