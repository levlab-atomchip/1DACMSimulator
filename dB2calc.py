# -*- coding: utf-8 -*-
"""
Created on Tue May 07 21:37:42 2013

@author: Will
"""

from math import pi, log, sqrt, exp, tan
from acmconstants import HBAR, MU_B, A, M

voxel_area = 1e-12

omega_0 = 2 * pi * 384.230e12 #Hz, from Steck
sigma0 = 2.907e-13 #m^2, from Steck
Gamma = 2 * pi * 6.0666e6 #Hz, from Steck
Isat = 16.69 #W/m^2, from Steck

omega_l = omega_0
domega_l = 0.01*Gamma
domega_0 = omega_0 * .01
dGamma = Gamma*.01

theta = pi/4
dtheta = theta * .01

delta = omega_l - omega_0

Il = Isat
dIl = Il * .01

Id = Il * .01
dId = Id * .1

Ia = Il * exp(-1)
#dIa = Il * .01
dIa = sqrt(dIl**2 + dId**2)



D = log((Il - Id)/(Ia - Id))

I = Il

sigma = sigma0 / (1 + 4*(delta / Gamma)**2 + I / Isat)

n = D / sigma


dn2 =                          ((dIl / (sigma * (Il - Id)))**2 + # Imaging Beam Intensity Noise
          ((Il - Ia)*dId / (sigma * (Il - Id) * (Ia - Id)))**2 + # Dark Current
                                (dIa / (sigma * (Ia - Id)))**2 + # Atom Image Fluctuations
     (8 * sigma * n * delta *domega_l/ (sigma0 * Gamma**2))**2 + # Laser Frequency Noise
                        (sigma * n * dIl / (sigma0 * Isat))**2 + # Imaging Beam Intensity Noise
((D * domega_0 / sigma**2)*(sigma / omega_0 + sigma**2 * 8 * delta / (sigma0 * Gamma**2)))**2 + # Resonance Frequency Noise
((D * dGamma / (sigma * Gamma))*(2*sigma*Il / (sigma0 * Isat) + 8*sigma*delta**2 / (sigma0 * Gamma**2) - 1)) +  # Atom Linewidth Noise
((2*tan(theta)*D*dtheta / sigma)*(sigma * Il / (sigma0 * Isat) - 1))**2)

dn = sqrt(dn2)

N = n * voxel_area
dN = dn * voxel_area

print 'Atoms per Voxel:   %4.1f'%N
print 'Atom Number Error: %4.1f'%dN
print "Error Percentage:  %4.1f "%(100*dn / n)

Ntot = 1e5
dNtot = Ntot * 0.05
G = (4 * pi * HBAR**2 * A) / M
omega_x = 2 * pi * 10 #Hz
domega_x = omega_x * .01
omega_perp = 2 * pi * 1000 #Hz
domega_perp = omega_perp * .01
voxel_l = 1e-6 #m

mu = 0.5*(15*G/(4*pi))**0.4 * M**0.6 * (Ntot*omega_perp**2 * omega_x)**0.4

dmu2 = ((0.4*mu)**2 * ((dNtot / Ntot)**2 + # Atom Number Noise
         (2*domega_perp / omega_perp)**2 + # Trap Transverse Frequency Noise
                 (domega_x / omega_x)**2)) # Trap Longitudinal Frequency Noise
dmu = sqrt(dmu2)

B = (HBAR * omega_perp / MU_B)*sqrt(1 + 4*A*N/voxel_l)
dB2 = (((2*A*HBAR*omega_perp*dN)/(voxel_l*MU_B*sqrt(1 + 4*A*N/voxel_l)))**2 + # Imaging Noise
                                          (B * domega_perp / omega_perp)**2 + # Trap Transverse Frequency Noise
                                                            (dmu / MU_B)**2)  # Chemical Potential Noise

dB = sqrt(dB2)

print '\n'
print 'Field:             %4.3f nT'%(B*1e9)
print 'Field Error:       %4.3f nT'%(dB*1e9)
print "Error Percentage:  %4.1f "%(100*dB / B)

ImgNoiseFactor = ((2*A*voxel_l/(B))*(HBAR*omega_perp / MU_B)**2)**2
muNoiseFactor = (0.4*mu/MU_B)**2
IlNoiseSS = ImgNoiseFactor * ((1 / (sigma * (Il - Id)))**2 + (D / (sigma0 * Isat))**2) * dIl**2
DarkNoiseSS = ImgNoiseFactor * ((Il - Ia) / (sigma * (Il - Id) * (Ia - Id)))**2 * dId**2
AtomImgSS = ImgNoiseFactor * (1 / (sigma * (Ia - Id)))**2 * dIa**2
omegaLSS = ImgNoiseFactor * (8 * D * delta / (sigma0 * Gamma**2))**2 * domega_l**2
#something breaks here when delta != 0
omega0SS = ImgNoiseFactor * ((D * domega_0 / sigma**2)*(sigma / omega_0 + sigma**2 * 8 * delta / (sigma0 * Gamma**2)))**2
GammaSS = ImgNoiseFactor * ((D * dGamma / (sigma * Gamma))*(2*sigma*Il / (sigma0 * Isat) + 8*sigma*delta**2 / (sigma0 * Gamma**2) - 1))
polarSS = ImgNoiseFactor * ((2*tan(theta)*D*dtheta / sigma)*(sigma * Il / (sigma0 * Isat) - 1))**2
AtomNSS = muNoiseFactor * (dNtot / Ntot)**2
omegaxSS = muNoiseFactor *(domega_x / omega_x)**2
omegaperpSS = muNoiseFactor * (2*domega_perp / omega_perp)**2 + (B * domega_perp / omega_perp)**2
totalSS = IlNoiseSS + DarkNoiseSS + AtomImgSS + omegaLSS + AtomNSS + omegaxSS + omegaperpSS

print '\n'
print 'Noise Source              Sum of Squares'
print '----------------------------------------'
print 'Img Beam Intensity:       %f'%(IlNoiseSS*1e18)
print 'Dark Current:             %f'%(DarkNoiseSS*1e18)
print 'Atom Image Noise:         %f'%(AtomImgSS*1e18)
print 'Laser Freq Noise:         %f'%(omegaLSS*1e18)
print 'Resonance Freq Noise:     %f'%(omega0SS*1e18)
print 'Linewidth Noise:          %f'%(GammaSS*1e18)
print 'Polarization Noise:       %f'%(polarSS*1e18)
print 'Atom # Noise:             %f'%(AtomNSS*1e18)
print 'omega x Noise:            %f'%(omegaxSS*1e18)
print 'omega perp Noise:         %f'%(omegaperpSS*1e18)
print '                         --------'
print 'Total SS:                 %f'%(totalSS*1e18)
print 'Field Error:              %f'%(sqrt(totalSS)*1e9)
