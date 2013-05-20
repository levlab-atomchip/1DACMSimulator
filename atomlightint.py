# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:38:52 2013

@author: Will
"""

from acmconstants import G1, ALPHA, D12, G2, C, HBAR, OMEGA_RES, LINEWIDTH_RES, CLOUD_THICKNESS
from math import pi
#import ImagingBeam
import numpy as np
import AtomImage
from Window import window
import matplotlib.pyplot as plt

def gH(omega, omega_resonance, linewidth):
    return (linewidth / (2*pi*((omega - omega_resonance)**2 + 0.25*linewidth**2)))
    
def atom_light_interaction(imaging_beam, atom_density):
    '''notation taken from "Atomic Physics" by Christopher Foot
    Produces image from atom density
    need to account for polarization!!'''
    #Isat = (pi*h*c)/(3*img_lambda**2*tau) #on resonance value
    A21 = (G1*4*ALPHA*((imaging_beam.omega)**3)*(D12**2)) / (G2*3*C**2)
#    print 'A21:'
#    print A21
    
#    abs_x_section = (2*pi**2*C**2*A21*gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES))
    abs_x_section = (3 * pi**2 * C**2 * A21 * gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES)) / (OMEGA_RES**2)
#    print 'lineshape factor:'
#    print gH(imaging_beam.omega, OMEGA_RES, LINEWIDTH_RES)
#    print 'x_section:'
#    print abs_x_section
    
    I_sat = (HBAR*imaging_beam.omega*A21)/(2*abs_x_section)
    
    I_0 = imaging_beam.get_slice(0)
    
#    abs_x_section_eff = abs_x_section/(1 + imaging_beam.intensity/I_sat) #actually varies in space
    abs_x_section_eff = np.array([abs_x_section/(1 + I/I_sat) for I in I_0])
#    print 'x_section:'
#    print abs_x_section_eff
#    plt.plot(window.window, abs_x_section_eff)
#    plt.title('abs_x_section_eff')
#    plt.show()
    #now exponentiate and multiply this by atom_density and imaging_beam to make a new image
    optical_density = abs_x_section_eff * atom_density.get_density()*CLOUD_THICKNESS
    I_f = I_0 * np.exp(-1*optical_density)
#    print 'I_0:'
#    print I_0
#    plt.plot(window.window, I_0)
#    plt.title('I_0')
#    plt.show()
    print 'OD:'
    print optical_density
#    plt.plot(window.window, optical_density)
#    plt.title('OD')
#    plt.show()
#    print 'I_f:'
#    print I_f
#    plt.plot(window.window, I_f)
#    plt.title('I_f')
#    plt.show()
    atom_image = AtomImage.AtomImage(I_f, imaging_beam)
    return atom_image