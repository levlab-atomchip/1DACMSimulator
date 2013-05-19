# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:15:38 2013

@author: Will
"""

namedtuple('ImagingBeam',['wavelength','intensity','linewidth', 'angle', 'focus','waist'])
''' wavelength / nm
    intensity / W/m2
    linewidth / Mhz
    angle / radian, from mirror plane
    focus / um, from atom cloud?
    waist / um '''
    
class ImagingBeam: 
    def __init__(self,wavelength, power, linewidth, angle, focus, waist):
        self.wavelength = wavelength
        self.power = power
        self.linewidth = linewidth
        self.angle = angle
        self.focus = focus
        self.waist = waist
        

        self.intensity = 2* self.power / (pi * waist**2)
        self.frequency = C / (wavelength * 1e-9)
        self.omega = 2 * pi * self.frequency
    def image_atoms(self, atom_cloud):
        ''' produce an AtomImage from an AtomCloud '''
        pass