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

import ImagingBeam
import CCD
import ImagingSystem
import AtomDensity
import matplotlib.pyplot as plt
from Window import window
from acmconstants import *
import numpy as np
    


class CurrentSlab: pass

class AtomChip: pass

class BField: pass
       
class ACMSimulator:
    def __init__(self):
#        self.current_slab = CurrentSlab(sample_file)
#        self.atom_chip = AtomChip(atomchip_file)
        self.atom_density = AtomDensity.AtomDensity(np.zeros(window.window.shape), 1e-6)
        self.imaging_beam = ImagingBeam.ImagingBeam(WAVELENGTH_RES, ISAT * 0.5, 10e6, 0, 0, 50e-6)
        self.ccd = CCD.CCD()
        self.imaging_system = ImagingSystem.ImagingSystem()
    
    def simulate(self):
#        mag_trap = AtomChip.get_trap()
#        perturbed_field = (self.current_slab.get_field(self.window) 
#                         + self.atom_chip.get_field(self.window))
#        perturbed_cloud = self.atom_density.mag_potential(perturbed_field)
        perturbed_cloud = self.atom_density
        atom_image = self.imaging_beam.image_atoms(perturbed_cloud)
        focused_image = self.imaging_system.image(atom_image)
        digital_image = self.ccd.image(focused_image)
        return digital_image
    
    def plot_result(self, digital_image):
        plt.plot(window.window, digital_image.image)
        plt.show()
        
acmsimulator = ACMSimulator()
result = acmsimulator.simulate()
acmsimulator.plot_result(result)
        
    
