# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:35:06 2013

@author: Will
"""
from Window import window
from acmconstants import M, G, HBAR, A, K_B
from math import pi, exp
import numpy as np
import logging

class AtomDensity:
    ''' 1D array of atom column density in trap '''
    def __init__(self, density_array, temperature):
        '''density_array in m^-3 '''
        self.density = density_array
        assert(len(self.density) == window.num_cells)
        self.temperature = temperature
        self.N_total = window.cell_size**3 * sum(self.density)
        
    def get_density(self):
        return self.density
        
    def harmonic_bec(self, omega_perp, omega_long):
        mu = (G * (15 / pi)**0.4 * (0.5)**(9.0 / 5.0) * (M / G)**0.6 * 
            self.N_total**0.4 * (omega_perp**2 * omega_long)**0.4)
        logging.debug("mu = %s"%mu)
        logging.debug('N = %d'%self.N_total)
        logging.debug('cell size = %f'%window.cell_size)
        harmonicBEC_density = np.array([(((mu - 0.5 * M * omega_long**2 * x**2) 
                                    / (HBAR * omega_perp))**2 - 1) 
                                    / (4 * A * window.cell_size**2) 
                                    for x in window.window])
        return AtomDensity(harmonicBEC_density, self.temperature)
        
    def harmonic_thermal(self, omega_perp, omega_long):
        w_perp2 = (2 * K_B * self.temperature / (M * omega_perp**2))
        w_long2 = (2 * K_B * self.temperature / (M * omega_long**2))
        n_0 = self.N_total / (pi**1.5 * w_perp2 * w_long2**0.5)
        harmonicThermal_density = np.array([n_0 * pi * w_perp2 * exp(-1 * x**2 / w_long2)
                                        / window.cell_size**2
                                        for x in window.window])
        return AtomDensity(harmonicThermal_density, self.temperature)
        
    def magtrap_approx(self, b_field, omega_perp, omega_long):
        mu = (G * (15 / pi)**0.4 * (0.5)**(9.0 / 5.0) * (M / G)**0.6 * 
            self.N_total**0.4 * (omega_perp**2 * omega_long)**0.4)
        logging.debug("mu = %s"%mu)
        logging.debug('N = %d'%self.N_total)
        logging.debug('cell size = %f'%window.cell_size)
        magtrap_density = np.array([(((mu - b_field.get_mag()) 
                                    / (HBAR * omega_perp))**2 - 1) 
                                    / (4 * A * window.cell_size**2) 
                                    for x in window.window])
        return AtomDensity(magtrap_density, self.temperature)