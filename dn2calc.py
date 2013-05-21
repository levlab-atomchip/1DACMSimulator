# -*- coding: utf-8 -*-
"""
Created on Tue May 07 20:07:04 2013

@author: Will
"""
from math import pi, log, sqrt, exp

voxel_area = 1e-12

omega_0 = 2 * pi * 384.230e12 #Hz
sigma0 = 2.907e-13 #m^2
Gamma = 2 * pi * 6.0666e6 #Hz
Isat = 16.69 #W/m^2

omega_l = omega_0
domega_l = 0.1*Gamma

delta = omega_l - omega_0

Il = Isat
dIl = Il * .01

Ia = Il * exp(-1)
dIa = Il * .01

Id = Il * .01
dId = Id * .1

D = log((Il - Id)/(Ia - Id))

I = Il

sigma = sigma0 / (1 + 4*(delta / Gamma)**2 + I / Isat)

n = D / sigma


dn2 = ((dIl / (sigma * (Il - Id)))**2 
    + ((Il - Ia)*dId / (sigma * (Il - Id) * (Ia - Id)))**2 
    + (dIa / (sigma * (Ia - Id)))**2 
    + (8 * sigma * n * delta *domega_l/ (sigma0 * Gamma**2))**2 
    + (sigma * n * dIl / (sigma0 * Isat))**2)
dn = sqrt(dn2)

N = n * voxel_area
dN = dn * voxel_area

print 'Atoms per Voxel:   %4.1f'%N
print 'Atom Number Error: %4.1f'%dN
print "Error Percentage:  %4.1f "%(100*dn / n)