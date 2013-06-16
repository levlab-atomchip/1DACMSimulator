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
#import AtomImage
from AtomImage import DigitalImage, Image
import matplotlib.pyplot as plt
from Window import window
from acmconstants import NUM_PIXELS, OMEGA_RES, C
from acmconstants import I_SAT, SIGMA_0, CLOUD_THICKNESS
import numpy as np
from math import pi

# Some test profiles
atom_linear = np.array([3e10*i for i in range(len(window.window))])
atom_tophat = np.array([0.1/window.cell_size**3 
                        for i in range(len(window.window))])
atom_tophat[0:512] = 1
atom_tophat[1536:] = 1

class CurrentSlab: pass

class AtomChip: pass

class BField: pass
       
class ACMSimulator:
    def __init__(self):
        self.atom_density = AtomDensity.AtomDensity(atom_tophat, 100e-9)
        self.imaging_beam = ImagingBeam.ImagingBeam((2*pi*C / (OMEGA_RES)), 
                                                    I_SAT*0.1*pi*(500e-6)**2, 
                                                    10e6, 
                                                    0, 
                                                    0, 
                                                    500e-6)
        self.ccd = CCD.CCD(NUM_PIXELS, (window.xmax - window.xmin) / NUM_PIXELS, 
                                       10, 
                                       0.07)
        self.imaging_system = ImagingSystem.ImagingSystem()
    
    def simulate(self):
        # field to cloud step not yet implemented
#        mag_trap = AtomChip.get_trap()
#        perturbed_field = (self.current_slab.get_field(self.window) 
#                         + self.atom_chip.get_field(self.window))
#        perturbed_cloud = self.atom_density.mag_potential(perturbed_field)
#        self.perturbed_cloud = self.atom_density.harmonicBEC(2e3, 10)
        self.perturbed_cloud = self.atom_density.harmonic_thermal(2e3, 100)
#        self.perturbed_cloud = self.atom_density
        self.atom_image = self.imaging_beam.image_atoms(self.perturbed_cloud)
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
    def plot_perturbed_cloud(self):
        plt.plot(window.window, self.perturbed_cloud.get_density())
        plt.title('Perturbed Cloud')
        plt.show()
    def plot_absorption_image(self):
        light_image = Image(self.imaging_beam.get_slice(0), window)
        digital_light_image = self.ccd.image(light_image, 1e-3)
        abs_image = np.log(digital_light_image.get_image_arr() / 
            self.digital_image.get_image_arr()) / (SIGMA_0 * CLOUD_THICKNESS)
        plt.plot(range(NUM_PIXELS), abs_image)
        plt.title('Absorption Image')
        plt.show()
    def plot_error(self):
        light_image = Image(self.imaging_beam.get_slice(0), window)
        digital_light_image = self.ccd.image(light_image, 1e-3)
        abs_image = DigitalImage(np.log(digital_light_image.get_image_arr() / 
            self.digital_image.get_image_arr()) / (SIGMA_0 * CLOUD_THICKNESS),
                                self.ccd)
#        window_res = (window.max - window.min) / window.num_cells)
        analog_abs_image = abs_image.get_analog((window.xmax - window.xmin)
                                                / window.num_cells)
#        print analog_abs_image.get_image_arr()
        error = np.abs((analog_abs_image.get_image_arr() * SIGMA_0 
        / self.imaging_beam.sigma()
                        - self.perturbed_cloud.get_density()) 
                        / self.perturbed_cloud.get_density())
        plt.plot(window.window, error)
#        plt.plot(window.window, self.atom_density.get_density())
        plt.title('error')
        plt.show()
        
        
acmsimulator = ACMSimulator()
result = acmsimulator.simulate()
acmsimulator.plot_result()
acmsimulator.plot_atom_image()
acmsimulator.plot_atom_density()
acmsimulator.plot_perturbed_cloud()
acmsimulator.plot_absorption_image()
acmsimulator.plot_error()