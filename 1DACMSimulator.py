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

from math import pi
from acmconstants import C
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
        

        self.intensity = 2* self.power / (pi * waist**2)
        self.frequency = C / (wavelength * 1e-9)
        self.omega = 2 * pi * self.frequency
    def image_atoms(self, atom_cloud):
        ''' produce an AtomImage from an AtomCloud '''
        pass
    


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
    
class DigitalImage:
    def __init__(self, image_array, CCD):
        pass
    
class CCD:
    def __init__(self, imaging_file):
        pass
#        self.resolution = resolution
#        self.nbits = nbits
        
    def image(self, atom_image):
        ''' produce a DigitalImage from an AtomImage '''
        pass
    
class ImagingSystem:
    def __init__(self, imaging_file):
        pass
    def image(self, atom_image):
        pass

class ACMSimulator:
    def __init__(self, sample_file, atomchip_file, atomcloud_file, imaging_file):
        self.current_slab = CurrentSlab(sample_file)
        self.atom_chip = AtomChip(atomchip_file)
        self.atom_density = AtomDensity(atomcloud_file)
        self.imaging_beam = ImagingBeam(imaging_file)
        self.ccd = CCD(imaging_file)
        self.imaging_system = ImagingSystem(imaging_file)
    
    def simulate(self):
#        mag_trap = AtomChip.get_trap()
        perturbed_field = (self.current_slab.get_field(self.window) 
                         + self.atom_chip.get_field(self.window))
        perturbed_cloud = self.atom_density.mag_potential(perturbed_field)
        atom_image = self.imaging_beam.image_atoms(perturbed_cloud)
        focused_image = self.imaging_system.image(atom_image)
        digital_image = self.ccd.image(focused_image)
        return digital_image
        
    
