# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:46:12 2013

@author: Will
"""

from acwires import HWire, VWire, NWire, HThinWire, VThinWire

from AtomChip import *

## Wire definition

# Horizontal Wires
hwires = []
vwires = []
nwires = []

hwires.append(HThinWire('Central Test Wire', 1, 1e-6, 1e-6, 1, 
                     -0.5, -0.5e-6, 0))

vwires.append(VThinWire('Arm 1', 0.5, 1e-6, 1e-6, 1, -0.001, -0.5, 0))
vwires.append(VThinWire('Arm 2', 0.5, 1e-6, 1e-6, 1,  0.001, 0, 0))

allwires = hwires + vwires + nwires

# 