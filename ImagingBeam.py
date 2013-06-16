# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:15:38 2013

@author: Will
"""

from acmconstants import C,SIGMA_0, I_SAT, OMEGA_RES, LINEWIDTH_RES
from math import pi, sqrt, exp
from Window import window 
import numpy as np
from atomlightint import atom_light_interaction
    
class ImagingBeam: 
    def __init__(self, wavelength, power, linewidth, angle, focus, waist_0):
        self.wavelength = wavelength
        self.power = power
        self.linewidth = linewidth
        self.angle = angle
        self.focus = focus
        self.waist_0 = waist_0
        

        self.I_0 = 2* self.power / (pi * waist_0**2)
        self.frequency = C / (wavelength)
        self.omega = 2 * pi * self.frequency
        self.rayleigh = pi * waist_0**2 / wavelength
    def gH(self, omega_resonance, linewidth):
        return (linewidth / (2*pi*((self.omega - omega_resonance)**2 
                                + 0.25*linewidth**2)))
    def sigma(self):
#        A21 = (G1*4*ALPHA*((self.omega)**3)*(D12**2)) / (G2*3*C**2)
#    print 'A21:'
#    print A21
#        abs_x_section = ((3 * pi**2 * C**2 * A21 * 
#                    self.gH(OMEGA_RES, LINEWIDTH_RES)) 
#                    / (OMEGA_RES**2))
#    print 'lineshape factor:'
#    print gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES)
#    print 'x_section:'
#    print abs_x_section
    
#        I_sat = (HBAR*self.omega*A21)/(2*abs_x_section)
    
        I_0 = self.get_slice(0)
        delta = self.omega - OMEGA_RES
        return np.array([SIGMA_0/(1 + 4*(delta/LINEWIDTH_RES)**2 + I/I_SAT) for I in I_0])
    def image_atoms(self, atom_cloud):
        ''' produce an AtomImage from an AtomCloud '''
        return atom_light_interaction(self, atom_cloud)
    
    def waist(self, z):
        return self.waist_0 * sqrt(1 + (z / self.rayleigh)**2)
        
    def intensity(self, r, z):
        w = self.waist(z)
        return self.I_0 * (self.waist_0 / w)**2 * exp(-2 * r**2 / w**2)
    def get_slice(self, z):
        '''produce a 1D line section through the center of the beam at z'''
        I = np.array([self.intensity(x, z) for x in window.window])
        
        return I