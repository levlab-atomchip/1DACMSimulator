# -*- coding: utf-8 -*-
"""

1D ACM Simulator

Set up current slab
find magnetic fields at trap
calculate true atom number density
optional: green laser binning
convert to image
imaging system operations (aperture, mag)
CCD binning


Created on Sun Apr 21 10:08:18 2013

@author: Will
"""

from collections import namedtuple

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
        
        #derive: intensity, frequency, omega

class CurrentSlab: pass

class AtomChip: pass

class BField: pass
       
class AtomDensity:
    ''' 1D array of atom density in trap '''
    def __init__(self, density_array, cell_size, temperature):
        ''' cell_size in um, density_array in um^-3 '''
        self.density = density_array
        self.cell_size = cell_size
        self.temperature = temperature
        
        self.length = len(self.density) * cell_size
        #self.psd = 
        
        
    
class AtomImage:
    ''' 1D array of light intensity after imaging '''
    def __init__(self, intensity_array, cell_size, imaging_beam):
        self.intensity = intensity_array
        self.cell_size = cell_size
        self.imaging_beam = imaging_beam
    
class DigitalImage: pass
    
class CCD: pass
    
class ImagingSystem: pass

class ACMSimulator:
    def __init__(self):
        self.current_slab = CurrentSlab()
        self.atom_chip = AtomChip()
        self.bfield = BField()
        self.atom_density = AtomDensity()
        self.atom_image = AtomImage()  
        self.ccd = CCD()
        self.imaging_system = ImagingSystem()
        self.digital_image = DigitalImage()
    
    def simulate(self): pass
        
    
