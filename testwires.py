# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:46:12 2013

@author: Will
"""

from acwires import HWire, VWire, NWire

#function [fin_horz_params, fin_vert_params, fin_norm_params] = Wire_Geometry_Specification()

from AtomChip import *

## Wire definition

# Horizontal Wires
#def __init__(self, name, length, width, height, current, subwires, xl, y0, z0):
hwires = []
vwires = []
nwires = []

hwires.append(HWire('Central Trapping Macrowire', l_trap, w_rad, h_rad, I_in, 
                    n, -l_trap / 2, -w_rad/2, -h_rad))

vwires.append(VWire( 'Left Axial Bias Lead Macrowire',  20e-3,  w_ax,  3e-3,  I_ax,  n,  -a_ax/2-w_ax/2,  -25e-3,  -3.1e-3))

allwires = hwires + vwires + nwires

# 