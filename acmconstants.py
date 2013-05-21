# -*- coding: utf-8 -*-
"""
Created on Thu May 02 21:43:22 2013

@author: Will
"""

from math import pi

# Physical Constants, from Steck Rb87 Alkali D Line Data
C = 2.99792e8 # m/s (exact)
ALPHA = 7.29735e-3 # from wikipedia
HBAR = 1.05457e-34 # J*sec
MU_B = 9.274e-24 # J/T
A_0 = 5.29e-11 #m, Bohr radius
MU_0 = 4*pi*1e-7


## Imaging Transition Properties
#THESE ARE WRONG!!!
G1 = 1
#D12 = 1.73135e-29 #C*m
D12 = 2.042*A_0
G2 = 1
OMEGA_RES = 2*pi*384.230e12 #Hz
LINEWIDTH_RES = 2*pi*6.0666e6 #Hz
WAVELENGTH_RES = 780e-9 #m
ISAT = 35.7 #W/m^2
SIGMA_0 = 1.356e-13 #m^2, resonant x section

# Rb87 Properties
A = 5.2e-9 #m, scattering length
M = 87 * 1.7e-27 #kg

# Dy Properties
#A = 100 * A_0
#M = 162.5 * 1.7e-27
#MU_B = 10* 9.274e-24

CLOUD_THICKNESS = 1e-6
BG_NOISE_CURRENT = 30 #e/p/s

# Camera Properties
# PIXIS 1024BR
PIXEL_SIZE = 13e-6 #m
NUM_PIXELS = 1024
DARK_CURRENT = .07 #e/p/s