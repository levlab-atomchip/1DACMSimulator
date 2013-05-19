# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:35:06 2013

@author: Will
"""
from Window import *

class AtomDensity:
    ''' 1D array of atom density in trap '''
    def __init__(self, density_array, temperature):
        ''' cell_size in um, density_array in um^-3 '''
        self.density = density_array
        assert(len(self.density) == window.num_cells)
        self.temperature = temperature