# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:35:06 2013

@author: Will
"""

class AtomDensity:
    ''' 1D array of atom density in trap '''
    def __init__(self, density_array, cell_size, temperature):
        ''' cell_size in um, density_array in um^-3 '''
        self.density = density_array
        self.cell_size = cell_size
        self.temperature = temperature
        
        self.length = len(self.density) * cell_size
        #self.psd =