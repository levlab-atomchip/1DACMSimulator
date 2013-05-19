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
from math import pi
    
atom_linear = np.array([3e16*i for i in range(len(window.window))])
atom_tophat = np.array([3e16 for i in range(len(window.window))])
atom_tophat[0:25] = 0
atom_tophat[75:] = 0

class CurrentSlab: pass

class AtomChip: pass

class BField: pass
       
class ACMSimulator:
    def __init__(self):
        self.atom_density = AtomDensity.AtomDensity(atom_tophat, 1e-6)
        self.imaging_beam = ImagingBeam.ImagingBeam((2*pi*C / OMEGA_RES), ISAT*0.05*pi*(500e-6)**2, 10e6, 0, 0, 500e-6)
        self.ccd = CCD.CCD()
        self.imaging_system = ImagingSystem.ImagingSystem()
    
    def simulate(self):
#        mag_trap = AtomChip.get_trap()
#        perturbed_field = (self.current_slab.get_field(self.window) 
#                         + self.atom_chip.get_field(self.window))
#        perturbed_cloud = self.atom_density.mag_potential(perturbed_field)
        perturbed_cloud = self.atom_density
        self.atom_image = self.imaging_beam.image_atoms(perturbed_cloud)
        focused_image = self.imaging_system.image(self.atom_image)
        digital_image = self.ccd.image(focused_image)
        return digital_image
    
    def plot_result(self, digital_image):
        plt.plot(window.window, digital_image.image)
        plt.title('Digital Image')
        plt.show()
    def plot_atom_image(self):
        plt.plot(window.window, self.atom_image.image)
        plt.title('Atom Image')
        plt.show()
    def plot_atom_density(self):
        plt.plot(window.window, self.atom_density.get_density())
        plt.title('Atom Density')
        plt.show()
    def plot_absorption_image(self):
        abs_image = np.log(self.imaging_beam.get_slice(0) / self.atom_image.image) / (SIGMA_0 * CLOUD_THICKNESS)
        plt.plot(window.window, abs_image)
        plt.title('Absorption Image')
        plt.show()
    def plot_error(self):
        abs_image = np.log(self.imaging_beam.get_slice(0) / self.atom_image.image) / (SIGMA_0 * CLOUD_THICKNESS)
        error = (abs_image - self.atom_density.get_density()) / self.atom_density.get_density()
        plt.plot(window.window, error)
        plt.title('error')
        plt.show()
acmsimulator = ACMSimulator()
result = acmsimulator.simulate()
acmsimulator.plot_result(result)
acmsimulator.plot_atom_image()
acmsimulator.plot_atom_density()
acmsimulator.plot_absorption_image()
acmsimulator.plot_error()