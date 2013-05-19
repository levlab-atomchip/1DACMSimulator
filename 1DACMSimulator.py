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
    


class CurrentSlab: pass

class AtomChip: pass

class BField: pass
       
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
        
    
