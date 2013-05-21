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
import AtomImage
import matplotlib.pyplot as plt
from Window import window
from acmconstants import *
import numpy as np
from math import pi
    
atom_linear = np.array([3e10*i for i in range(len(window.window))])
atom_tophat = np.array([3e12 for i in range(len(window.window))])
atom_tophat[0:512] = 0
atom_tophat[1536:] = 0

class CurrentSlab: pass

class AtomChip: pass

class BField: pass
       
class ACMSimulator:
    def __init__(self):
        self.atom_density = AtomDensity.AtomDensity(atom_tophat, 1e-6)
        self.imaging_beam = ImagingBeam.ImagingBeam((2*pi*C / OMEGA_RES), ISAT*0.01*pi*(500e-6)**2, 10e6, 0, 0, 500e-6)
        self.ccd = CCD.CCD(NUM_PIXELS, (window.max - window.min) / NUM_PIXELS, 10, 0.07)
        self.imaging_system = ImagingSystem.ImagingSystem()
    
    def simulate(self):
#        mag_trap = AtomChip.get_trap()
#        perturbed_field = (self.current_slab.get_field(self.window) 
#                         + self.atom_chip.get_field(self.window))
#        perturbed_cloud = self.atom_density.mag_potential(perturbed_field)
        perturbed_cloud = self.atom_density
        self.atom_image = self.imaging_beam.image_atoms(perturbed_cloud)
        focused_image = self.imaging_system.image(self.atom_image)
        self.digital_image = self.ccd.image(focused_image, 1000e-6)
        return self.digital_image
    
    def plot_result(self):
        plt.plot(range(NUM_PIXELS), self.digital_image.get_image_arr())
        plt.title('Digital Image')
        plt.show()
    def plot_atom_image(self):
        plt.plot(window.window, self.atom_image.get_image_arr())
        plt.title('Atom Image')
        plt.show()
    def plot_atom_density(self):
        plt.plot(window.window, self.atom_density.get_density())
        plt.title('Atom Density')
        plt.show()
    def plot_absorption_image(self):
        light_image = AtomImage.Image(self.imaging_beam.get_slice(0), window)
        digital_light_image = self.ccd.image(light_image, 1e-3)
        abs_image = np.log(digital_light_image.get_image_arr() / 
            self.digital_image.get_image_arr()) / (SIGMA_0 * CLOUD_THICKNESS)
        plt.plot(range(NUM_PIXELS), abs_image)
        plt.title('Absorption Image')
        plt.show()
    def plot_error(self):
<<<<<<< HEAD

=======
>>>>>>> 141f3f5e98123d92404dfd6f47bd09c647093dce
        light_image = AtomImage.Image(self.imaging_beam.get_slice(0), window)
        digital_light_image = self.ccd.image(light_image, 1e-3)
        abs_image = np.log(digital_light_image.get_image_arr() / 
            self.digital_image.get_image_arr()) / (SIGMA_0 * CLOUD_THICKNESS)
        analog_abs_image = abs_image.get_analog((window.max - window.min
                                                / window.num_cells))
#        abs_image = np.log(self.imaging_beam.get_slice(0) / self.atom_image.image) / (SIGMA_0 * CLOUD_THICKNESS)
        error = np.abs((analog_abs_image - self.atom_density.get_density()) 
                                    / self.atom_density.get_density())
        plt.plot(window.window, error)
#        plt.plot(window.window, self.atom_density.get_density())
#        plt.scatter(np.linspace(window.min, window.max, NUM_PIXELS), abs_image)
        plt.title('error')
        plt.show()
        
        
acmsimulator = ACMSimulator()
result = acmsimulator.simulate()
acmsimulator.plot_result()
acmsimulator.plot_atom_image()
acmsimulator.plot_atom_density()
acmsimulator.plot_absorption_image()
acmsimulator.plot_error()