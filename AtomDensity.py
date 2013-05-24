# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:35:06 2013

@author: Will
"""
from Window import window

class AtomDensity:
    ''' 1D array of atom column density in trap '''
    def __init__(self, density_array, temperature):
        '''density_array in m^-3 '''
        self.density = density_array
        assert(len(self.density) == window.num_cells)
        self.temperature = temperature
    def get_density(self):
        return self.density