# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:29:28 2013

@author: Will
"""

class AtomImage:
    ''' 1D array of light intensity after imaging '''
    def __init__(self, intensity_array, cell_size, imaging_beam):
        self.intensity = intensity_array
        self.cell_size = cell_size
        self.imaging_beam = imaging_beam