# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:35:06 2013

@author: Will
"""
from Window import window
from acmconstants import M, G, HBAR, A
from math import pi

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
	def 1D_harmonic(self, omega_perp, omega_long):
		mu = G * (15 / pi)**0.4 * (0.5)**(9.0 / 5.0) * (M / G)**0.6 * self.N_total**0.4 * (omega_perp**2 * omega_long)**0.4
		1D_harmonic_density = np.array([(((mu - 0.5 * M * omega_long**2 * x**2) / (HBAR * omega_perp))**2 - 1) / (4 * A) for x in window.window])
		return 1D_harmonic_density