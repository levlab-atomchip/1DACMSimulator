# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:46:12 2013

@author: Will
"""

from acwires import HThinWire, VThinWire, NWire


from AtomChip import *

## Wire definition

# Horizontal Wires
hwires = []
vwires = []
nwires = []

hwires.append(HThinWire('Central Trapping Macrowire', l_trap, w_rad, h_rad, I_in, 
                    -l_trap / 2, -w_rad/2, -h_rad))


hwires.append(HThinWire('Left Central Trapping Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    I_in, -25e-3, -w_rad/2, -2.1e-3))


hwires.append(HThinWire('Right Central Trapping Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    I_in, 6.75e-3, -w_rad/2, -2.1e-3))


hwires.append(HThinWire('Upper Bias Macrowire', 
                    l_trap, w_rad, h_rad, 
                    I_in, -l_trap/2, -w_rad/2, -h_rad))

hwires.append(HThinWire('Right Upper Bias Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    -I_out, 6.75e-3, a-w_rad/2, -2.1e-3))


hwires.append(HThinWire('Left Upper Bias Macrowire Lead', 
                    18.25e-3, w_rad, 2e-3, 
                    -I_out, -25e-3, a-w_rad/2, -2.1e-3))


hwires.append(HThinWire('Lower Bias Macrowire', 
                    l_trap, w_rad, h_rad, 
                    -I_out, -l_trap/2, -a-w_rad/2, -h_rad))


hwires.append(HThinWire('Right Lower Bias Macrowire Lead', 
                    33.25e-3, w_rad, 2e-3, 
                    -I_out, 6.75e-3,-a-w_rad/2, -2.1e-3))


hwires.append(HThinWire('Left Lower Bias Macrowire Lead', 
                    33.25e-3, w_rad, 2e-3, 
                    -I_out, -40e-3,-a-w_rad/2, -2.1e-3))


hwires.append(HThinWire('Central Microwire', 
                    4e-3, w_micro, h_micro, 
                    I_micro_trap, -2e-3, -w_micro/2, chip_height))


hwires.append(HThinWire('Left Central Lead Microwire', 
                    3e-3, w_micro_lead, h_micro, 
                    I_micro_trap, -5e-3, -w_micro_lead/2, chip_height))


hwires.append(HThinWire('Left Central Thick Lead Microwire', 
                    7.5e-3, w_micro_thlead, h_micro, 
                    I_micro_trap, -12.5e-3, -w_micro_thlead/2, chip_height))


hwires.append(HThinWire('Right Central Lead Microwire', 
                    3e-3, w_micro_lead, h_micro, 
                    I_micro_trap, 2e-3, -w_micro_lead/2, chip_height))


hwires.append(HThinWire('Right Central Thick Lead Microwire', 
                    7.5e-3, w_micro_thlead, h_micro, 
                    I_micro_trap, 5e-3, -w_micro_thlead/2, chip_height))


hwires.append(HThinWire('Left Arm Microwire', 
                    1e-3-w_micro/2, w_micro, h_micro, 
                    -I_micro_arm, -2e-3, -1.5*w_micro - sp, chip_height))


hwires.append(HThinWire('Left Arm Lead Microwire', 
                    3e-3, w_micro_lead, h_micro,  
                    -I_micro_arm, 
                    -5e-3, -1.5*w_micro_lead - sp, chip_height))

hwires.append(HThinWire('Left Arm Thick Lead Microwire', 
                    6.5e-3, w_micro_thlead, h_micro, 
                    -I_micro_arm, 
                    -11.5e-3, -1.5*w_micro_thlead - sp, chip_height))


hwires.append(HThinWire('Left Arm Return Microwire', 
                    4e-3-w_micro/2, w_micro_lead, h_micro,  
                    I_micro_arm, 
                    -5e-3, -5e-3, chip_height))


hwires.append(HThinWire('Left Arm Thick Return Microwire', 
                    4e-3, w_micro_thlead, h_micro,  
                    I_micro_arm, -9.5e-3, -5e-3, chip_height))


hwires.append(HThinWire('Right Arm Microwire', 
                    1e-3-w_micro/2, w_micro, h_micro, 
                    -I_micro_arm, 
                    l_med/2 + w_micro/2, sp+w_micro/2, chip_height))


hwires.append(HThinWire('Right Arm Lead Microwire', 
                    3e-3-w_micro/2,w_micro_lead, h_micro, 
                    -I_micro_arm, 
                    2e-3, w_micro_lead/2 + sp, chip_height))


hwires.append(HThinWire( 'Right Arm Thick Lead Microwire',  
                    6.5e-3-w_micro/2,  w_micro_thlead,  h_micro,  
                    -I_micro_arm,   
                    2e-3,  w_micro_thlead/2 + sp,  chip_height))

hwires.append(HThinWire( 'Right Arm Return Microwire',  
                    4e-3,  w_micro_lead,  h_micro,  
                    I_micro_arm,   
                    l_med/2 + w_micro/2,  4.5e-3,  chip_height))

hwires.append(HThinWire( 'Right Arm Thick Return Microwire',  
                    15.75e-3,  w_micro_thlead,  h_micro,  
                    I_micro_arm,   
                    5e-3,  3.5e-3,  chip_height))


hwires.append(HThinWire( 'Dimple Microwire',  
                    (l_micro - w_micro)/2 ,  w_micro,  h_micro,  
                    -I_micro_dimple,   
                    -l_micro/2,  w_micro/2 + sp,  chip_height))

hwires.append(HThinWire( 'Left Axial Lead Macrowire',  
                    19.25e-3 ,  0, 0,  
                    I_ax,  
                    -25e-3,  -25e-3,  0))

hwires.append(HThinWire( 'Right Axial Lead Macrowire',  
                    19.25e-3 ,  0, 0,  
                    -I_ax,   
                    5.75e-3,  -25e-3,  0))


# Vertical Wires

vwires.append(VThinWire( 'Left Axial Bias Macrowire',  
                    l_ax,  w_ax,  h_ax,  
                    I_ax,   
                    -a_ax/2-w_ax/2,  
                    -l_ax/2,  -sub - h_ax/2))


vwires.append(VThinWire( 'Left Axial Bias Lead Macrowire',  
                    20e-3,  w_ax,  3e-3,  
                    I_ax,   
                    -a_ax/2-w_ax/2,  -25e-3,  -3.1e-3))

vwires.append(VThinWire( 'Right Axial Bias Macrowire',  
                    l_ax,  w_ax,  h_ax,  
                    I_ax,   
                    a_ax/2-w_ax/2,  -l_ax/2,  -sub - h_ax/2))

vwires.append(VThinWire( 'Right Axial Bias Lead Macrowire',  
                    20e-3,  w_ax,  3e-3,  
                    I_ax,  
                    a_ax/2-w_ax/2,  -25e-3,  -3.1e-3))

vwires.append(VThinWire( 'Axial Dimple Macrowire',  
                    l_ax,  w_dimple,  h_dimple,  
                    I_dimple,   
                    -w_dimple/2,  -l_ax/2,  -sub - h_dimple/2))

vwires.append(VThinWire( 'Axial Dimple Lead Macrowire',  
                    20e-3,  w_dimple,  3e-3,  
                    I_dimple,   
                    -w_dimple/2,  -25e-3,  -3.1e-3))

vwires.append(VThinWire( 'Left Bias Lead Macrowire',  
                    2.75e-3,  w_rad,  h_ax,  
                    -I_out,   
                    -24.25e-3-w_rad/2,  -6e-3,  -sub-h_ax/2))

vwires.append(VThinWire( 'Right Bias Lead Macrowire',  
                    2.75e-3,  w_rad,  h_ax,  
                    I_out,   
                    24.25e-3-w_rad/2,  -6e-3,  -sub-h_ax/2))

vwires.append(VThinWire( 'Left Central Lead Macrowire', 
                    13e-3,  w_rad,  3e-3,  
                    I_in,   
                    -24.25e-3-w_rad/2,  -13e-3,  -10e-3))

vwires.append(VThinWire( 'Right Central Lead Macrowire',  
                    13e-3,  w_rad,  3e-3,  
                    -I_in,   
                    24.25e-3-w_rad/2,  -13e-3,  -10e-3))

vwires.append(VThinWire( 'Left Central Thick Lead Microwire',  
                    11.5e-3,  w_micro_thlead,  h_micro,  
                    I_micro_trap,   
                    -12.75e-3,  -11e-3,  chip_height))

vwires.append(VThinWire( 'Right Central Thick Lead Microwire',  
                    11.5e-3,  w_micro_thlead,  h_micro,  
                    -I_micro_trap,   
                    11.75e-3,  -11e-3,  chip_height))

vwires.append(VThinWire( 'Left Arm Microwire',  
                    l_arms-(w_micro/2 + sp),  w_micro,  h_micro, 
                    I_micro_arm,   
                    -l_med/2 - w_micro/2,  -l_arms,  chip_height))

vwires.append(VThinWire( 'Left Arm Thick Lead Microwire',  
                    12.5e-3,  w_micro_thlead,  h_micro, 
                    -I_micro_arm,   
                    -11.75e-3,  -13e-3,  chip_height))

vwires.append(VThinWire( 'Left Arm Thick Return Microwire',  
                    12e-3,  w_micro_thlead,  h_micro,  
                    I_micro_arm,   
                    -10e-3,  -16e-3,  chip_height))

vwires.append(VThinWire( 'Right Arm Microwire',  
                    l_arms-(w_micro/2 + sp),  w_micro,  h_micro,  
                    I_micro_arm,   
                    l_med/2 - w_micro/2,  w_micro/2 + sp,  chip_height))

vwires.append(VThinWire( 'Right Arm Thick Lead Microwire',  
                    12.5e-3,  w_micro_thlead,  h_micro,  
                    I_micro_arm,   
                    12.75e-3,  -13e-3,  chip_height))

vwires.append(VThinWire( 'Right Arm Thick Return Microwire',  
                    10e-3,  w_micro_thlead,  h_micro,  
                    -I_micro_arm,   
                    15e-3,  -6e-3,  chip_height))

vwires.append(VThinWire( 'Dimple Microwire',  
                    l_arms-(w_micro/2 + sp),  w_micro,  h_micro,  
                    -I_micro_dimple,   
                    -w_micro/2,  w_micro/2 + sp,  chip_height))

nwires.append(NWire( 'Left Upper Bias Lead Rod', 
                    40e-2,  0,  0,  
                    -I_out,  
                    -40e-3,  0,  -40e-2))

nwires.append(NWire( 'Right Upper Bias Lead Rod', 
                    40e-2,  0,  0,  
                    I_out,   
                    40e-3,  0,  -40e-2))

nwires.append(NWire( 'Left Lower Bias Lead Rod', 
                    390e-3,  0,  0,  
                    -I_out,  
                    -30e-3,  0,  -40e-2))

nwires.append(NWire( 'Right Lower Bias Lead Rod', 
                    390e-3,  0,  0,  
                    I_out,  
                    30e-3,  0,  -40e-2))

allwires = hwires + vwires + nwires