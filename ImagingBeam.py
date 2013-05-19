# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:15:38 2013

@author: Will
"""

#namedtuple('ImagingBeam',['wavelength','intensity','linewidth', 'angle', 'focus','waist'])
#''' wavelength / nm
#    intensity / W/m2
#    linewidth / Mhz
#    angle / radian, from mirror plane
#    focus / um, from atom cloud?
#    waist / um '''
    
from acmconstants import C
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
        self.frequency = C / (wavelength * 1e-9)
        self.omega = 2 * pi * self.frequency
        self.rayleigh = pi * waist_0**2 / wavelength
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