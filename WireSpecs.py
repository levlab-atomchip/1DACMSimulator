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
#n_hwires = 0
#n_hsubwires = 0
#i = 1

#hwire(i).name = 'Central Trapping Macrowire'
#hwire(i).xl = -l_trap/2
#hwire(i).length = l_trap
#hwire(i).y0 = -w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -h_rad
#hwire(i).height = h_rad
#hwire(i).current = I_in
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Central Trapping Macrowire', l_trap, w_rad, h_rad, I_in, 
                    n, -l_trap / 2, -w_rad/2, -h_rad))

#hwire(i).name = 'Left Central Trapping Macrowire Lead'
#hwire(i).xl = -25e-3
#hwire(i).length = 18.25e-3
#hwire(i).y0 = -w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -2.1e-3
#hwire(i).height = 2e-3
#hwire(i).current = I_in
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Central Trapping Macrowire Lead', 18.25e-3, w_rad, 2e-3, I_in, 
                    n, -25e-3, -w_rad/2, -2.1e-3))

#hwire(i).name = 'Right Central Trapping Macrowire Lead'
#hwire(i).xl = 6.75e-3
#hwire(i).length = 18.25e-3
#hwire(i).y0 = -w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -2.1e-3
#hwire(i).height = 2e-3
#hwire(i).current = I_in
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Right Central Trapping Macrowire Lead', 18.25e-3, w_rad, 2e-3, I_in, 
                    n, 6.75e-3, -w_rad/2, -2.1e-3))


#hwire(i).name = 'Upper Bias Macrowire'
#hwire(i).xl = -l_trap/2
#hwire(i).length = l_trap
#hwire(i).y0 = a-w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -h_rad
#hwire(i).height = h_rad
#hwire(i).current = -I_out
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Upper Bias Macrowire', l_trap, w_rad, h_rad, I_in, 
                    n, -l_trap/2, -w_rad/2, -h_rad))

#hwire(i).name = 'Right Upper Bias Macrowire Lead'
#hwire(i).xl = 6.75e-3
#hwire(i).length = 18.25e-3
#hwire(i).y0 = a-w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -2.1e-3
#hwire(i).height = 2e-3
#hwire(i).current = -I_out
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Right Upper Bias Macrowire Lead', 18.25e-3, w_rad, 2e-3, -I_out, 
                    n, 6.75e-3, a-w_rad/2, -2.1e-3))

#hwire(i).name = 'Left Upper Bias Macrowire Lead'
#hwire(i).xl = -25e-3
#hwire(i).length = 18.25e-3
#hwire(i).y0 = a-w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -2.1e-3
#hwire(i).height = 2e-3
#hwire(i).current = -I_out
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Upper Bias Macrowire Lead', 18.25e-3, w_rad, 2e-3, -I_out, 
                    n, -25e-3, a-w_rad/2, -2.1e-3))

#hwire(i).name = 'Lower Bias Macrowire'
#hwire(i).xl = -l_trap/2
#hwire(i).length = l_trap
#hwire(i).y0 = -a-w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -h_rad
#hwire(i).height = h_rad
#hwire(i).current = -I_out
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Lower Bias Macrowire', l_trap, w_rad, h_rad, -I_out, 
                    n, -l_trap/2, -a-w_rad/2, -h_rad))

#hwire(i).name = 'Right Lower Bias Macrowire Lead'
#hwire(i).xl = 6.75e-3
#hwire(i).length = 33.25e-3
#hwire(i).y0 = -a-w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -2.1e-3
#hwire(i).height = 2e-3
#hwire(i).current = -I_out
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Right Lower Bias Macrowire Lead', 33.25e-3, w_rad, 2e-3, -I_out, 
                    n, 6.75e-3,-a-w_rad/2, -2.1e-3))

#hwire(i).name = 'Left Lower Bias Macrowire Lead'
#hwire(i).xl = -40e-3
#hwire(i).length = 33.25e-3
#hwire(i).y0 = -a-w_rad/2
#hwire(i).width = w_rad
#hwire(i).z0 = -2.1e-3
#hwire(i).height = 2e-3
#hwire(i).current = -I_out
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Lower Bias Macrowire Lead', 33.25e-3, w_rad, 2e-3, -I_out, 
                    n, -40e-3,-a-w_rad/2, -2.1e-3))

#hwire(i).name = 'Central Microwire'
#hwire(i).xl = -2e-3
#hwire(i).length = 4e-3
#hwire(i).y0 = -w_micro/2
#hwire(i).width = w_micro
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_trap
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Central Microwire', 4e-3, w_micro, h_micro, I_micro_trap, 
                    n, -2e-3, -w_micro/2, chip_height))

#hwire(i).name = 'Left Central Lead Microwire'
#hwire(i).xl = -5e-3
#hwire(i).length = 3e-3
#hwire(i).y0 = -w_micro_lead/2
#hwire(i).width = w_micro_lead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_trap
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Central Lead Microwire', 3e-3, w_micro_lead, h_micro, I_micro_trap, 
                    n, -5e-3, -w_micro_lead/2, chip_height))

#hwire(i).name = 'Left Central Thick Lead Microwire'
#hwire(i).xl = -12.5e-3
#hwire(i).length = 7.5e-3
#hwire(i).y0 = -w_micro_thlead/2
#hwire(i).width = w_micro_thlead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_trap
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Central Thick Lead Microwire', 7.5e-3, w_micro_thlead, h_micro, I_micro_trap, 
                    n, -12.5e-3, -w_micro_thlead/2, chip_height))

#hwire(i).name = 'Right Central Lead Microwire'
#hwire(i).xl = 2e-3
#hwire(i).length = 3e-3
#hwire(i).y0 = -w_micro_lead/2
#hwire(i).width = w_micro_lead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_trap
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Right Central Lead Microwire', 3e-3, w_micro_lead, h_micro, I_micro_trap, 
                    n, 2e-3, -w_micro_lead/2, chip_height))

#hwire(i).name = 'Right Central Thick Lead Microwire'
#hwire(i).xl = 5e-3
#hwire(i).length = 7.5e-3
#hwire(i).y0 = -w_micro_thlead/2
#hwire(i).width = w_micro_thlead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_trap
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Right Central Thick Lead Microwire', 7.5e-3, w_micro_thlead, h_micro, I_micro_trap, 
                    n, 5e-3, -w_micro_thlead/2, chip_height))

#hwire(i).name = 'Left Arm Microwire'
#hwire(i).xl = -2e-3
#hwire(i).length = 1e-3-w_micro/2 
#hwire(i).y0 = -1.5*w_micro - sp
#hwire(i).width = w_micro
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = -I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Arm Microwire', 1e-3-w_micro/2, w_micro, h_micro, -I_micro_arm, 
                    n, -2e-3, -1.5*w_micro - sp, chip_height))

#hwire(i).name = 'Left Arm Lead Microwire'
#hwire(i).xl = -5e-3
#hwire(i).length = 3e-3 
#hwire(i).y0 = -1.5*w_micro_lead - sp
#hwire(i).width = w_micro_lead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = -I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Arm Lead Microwire', 3e-3, w_micro_lead, h_micro,  -I_micro_arm, 
                    n, -5e-3, -1.5*w_micro_lead - sp, chip_height))

#hwire(i).name = 'Left Arm Thick Lead Microwire'
#hwire(i).xl = -11.5e-3
#hwire(i).length = 6.5e-3 
#hwire(i).y0 = -1.5*w_micro_thlead - sp
#hwire(i).width = w_micro_thlead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = -I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Arm Thick Lead Microwire', 6.5e-3, w_micro_thlead, h_micro, -I_micro_arm, 
                    n, -11.5e-3, -1.5*w_micro_thlead - sp, chip_height))

#hwire(i).name = 'Left Arm Return Microwire'
#hwire(i).xl = -5e-3
#hwire(i).length = 4e-3-w_micro/2 
#hwire(i).y0 = -5e-3
#hwire(i).width = w_micro_lead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Arm Return Microwire', 4e-3-w_micro/2, w_micro_lead, h_micro,  I_micro_arm, 
                    n, -5e-3, -5e-3, chip_height))

#hwire(i).name = 'Left Arm Thick Return Microwire'
#hwire(i).xl = -9.5e-3
#hwire(i).length = 4e-3
#hwire(i).y0 = -5e-3
#hwire(i).width = w_micro_thlead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Left Arm Thick Return Microwire', 4e-3, w_micro_thlead, h_micro,  I_micro_arm, 
                    n, -9.5e-3, -5e-3, chip_height))

#hwire(i).name = 'Right Arm Microwire'
#hwire(i).xl = l_med/2 + w_micro/2
#hwire(i).length = 1e-3-w_micro/2
#hwire(i).y0 = sp+w_micro/2
#hwire(i).width = w_micro
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = -I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Right Arm Microwire', 1e-3-w_micro/2, w_micro, h_micro, -I_micro_arm, 
                    n, l_med/2 + w_micro/2, sp+w_micro/2, chip_height))

#hwire(i).name = 'Right Arm Lead Microwire'
#hwire(i).xl = 2e-3
#hwire(i).length = 3e-3-w_micro/2
#hwire(i).y0 = w_micro_lead/2 + sp
#hwire(i).width = w_micro_lead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = -I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire('Right Arm Lead Microwire', 3e-3-w_micro/2,w_micro_lead, h_micro, -I_micro_arm, 
                    n, 2e-3, w_micro_lead/2 + sp, chip_height))

#hwire(i).name = 'Right Arm Thick Lead Microwire'
#hwire(i).xl = 2e-3
#hwire(i).length = 6.5e-3-w_micro/2
#hwire(i).y0 = w_micro_thlead/2 + sp
#hwire(i).width = w_micro_thlead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = -I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
hwires.append(HWire( 'Right Arm Thick Lead Microwire',  6.5e-3-w_micro/2,  
                    w_micro_thlead,  h_micro,  -I_micro_arm,  n,  2e-3,  
                    w_micro_thlead/2 + sp,  chip_height))

#hwire(i).name = 'Right Arm Return Microwire'
#hwire(i).xl = l_med/2 + w_micro/2
#hwire(i).length = 4e-3
#hwire(i).y0 = 4.5e-3
#hwire(i).width = w_micro_lead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
#
#hwire(i).name = 'Right Arm Thick Return Microwire'
#hwire(i).xl = 5e-3
#hwire(i).length = 15.75e-3
#hwire(i).y0 = 3.5e-3
#hwire(i).width = w_micro_thlead
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = I_micro_arm
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1

hwires.append(HWire( 'Right Arm Return Microwire',  4e-3,  w_micro_lead,  h_micro,  I_micro_arm,  n,  l_med/2 + w_micro/2,  4.5e-3,  chip_height))

hwires.append(HWire( 'Right Arm Thick Return Microwire',  15.75e-3,  w_micro_thlead,  h_micro,  I_micro_arm,  n,  5e-3,  3.5e-3,  chip_height))

#hwire(i).name = 'Dimple Microwire'
#hwire(i).xl = -l_micro/2
#hwire(i).length = (l_micro - w_micro)/2 
#hwire(i).y0 = w_micro/2 + sp
#hwire(i).width = w_micro
#hwire(i).z0 = chip_height
#hwire(i).height = h_micro
#hwire(i).current = -I_micro_dimple
#hwire(i).subwires = n
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
#
#hwire(i).name = 'Left Axial Lead Macrowire'
#hwire(i).xl = -25e-3
#hwire(i).length = 19.25e-3 
#hwire(i).y0 = -25e-3
#hwire(i).width = 0
#hwire(i).z0 = 0
#hwire(i).height =0
#hwire(i).current = I_ax
#hwire(i).subwires = 1
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1
#
#hwire(i).name = 'Right Axial Lead Macrowire'
#hwire(i).xl = 5.75e-3
#hwire(i).length = 19.25e-3 
#hwire(i).y0 = -25e-3
#hwire(i).width = 0
#hwire(i).z0 = 0
#hwire(i).height =0
#hwire(i).current = -I_ax
#hwire(i).subwires = 1
#n_hwires = n_hwires + 1
#n_hsubwires = n_hsubwires + hwire(i).subwires^2
#i = i + 1

hwires.append(HWire( 'Dimple Microwire',  (l_micro - w_micro)/2 ,  w_micro,  h_micro,  -I_micro_dimple,  n,  -l_micro/2,  w_micro/2 + sp,  chip_height))

hwires.append(HWire( 'Left Axial Lead Macrowire',  19.25e-3 ,  0, 0,  I_ax,  1,  -25e-3,  -25e-3,  0))

hwires.append(HWire( 'Right Axial Lead Macrowire',  19.25e-3 ,  0, 0,  -I_ax,  1,  5.75e-3,  -25e-3,  0))


# Vertical Wires
n_vwires = 0
n_vsubwires = 0
i = 1

#vwire(i).name = 'Left Axial Bias Macrowire'
#vwire(i).yd = -l_ax/2
#vwire(i).length = l_ax
#vwire(i).x0 = -a_ax/2-w_ax/2
#vwire(i).width = w_ax
#vwire(i).z0 = -sub - h_ax/2
#vwire(i).height = h_ax
#vwire(i).current = I_ax
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
vwires.append(VWire( 'Left Axial Bias Macrowire',  l_ax,  w_ax,  h_ax,  I_ax,  n,  -a_ax/2-w_ax/2,  -l_ax/2,  -sub - h_ax/2))

#vwire(i).name = 'Left Axial Bias Lead Macrowire'
#vwire(i).yd = -25e-3
#vwire(i).length = 20e-3
#vwire(i).x0 = -a_ax/2-w_ax/2
#vwire(i).width = w_ax
#vwire(i).z0 = -3.1e-3
#vwire(i).height = 3e-3
#vwire(i).current = I_ax
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Axial Bias Macrowire'
#vwire(i).yd = -l_ax/2
#vwire(i).length = l_ax
#vwire(i).x0 = a_ax/2-w_ax/2
#vwire(i).width = w_ax
#vwire(i).z0 = -sub - h_ax/2
#vwire(i).height = h_ax
#vwire(i).current = I_ax
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Axial Bias Lead Macrowire'
#vwire(i).yd = -25e-3
#vwire(i).length = 20e-3
#vwire(i).x0 = a_ax/2-w_ax/2
#vwire(i).width = w_ax
#vwire(i).z0 = -3.1e-3
#vwire(i).height = 3e-3
#vwire(i).current = I_ax
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Axial Dimple Macrowire'
#vwire(i).yd = -l_ax/2
#vwire(i).length = l_ax
#vwire(i).x0 = -w_dimple/2
#vwire(i).width = w_dimple
#vwire(i).z0 = -sub - h_dimple/2
#vwire(i).height = h_dimple
#vwire(i).current = I_dimple
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Axial Dimple Lead Macrowire'
#vwire(i).yd = -25e-3
#vwire(i).length = 20e-3
#vwire(i).x0 = -w_dimple/2
#vwire(i).width = w_dimple
#vwire(i).z0 = -3.1e-3
#vwire(i).height = 3e-3
#vwire(i).current = I_dimple
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Left Bias Lead Macrowire'
#vwire(i).yd = -6e-3
#vwire(i).length = 2.75e-3
#vwire(i).x0 = -24.25e-3-w_rad/2
#vwire(i).width = w_rad
#vwire(i).z0 = -sub-h_ax/2
#vwire(i).height = h_ax
#vwire(i).current = -I_out
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Bias Lead Macrowire'
#vwire(i).yd = -6e-3
#vwire(i).length = 2.75e-3
#vwire(i).x0 = 24.25e-3-w_rad/2
#vwire(i).width = w_rad
#vwire(i).z0 = -sub-h_ax/2
#vwire(i).height = h_ax
#vwire(i).current = I_out
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Left Central Lead Macrowire'
#vwire(i).yd = -13e-3
#vwire(i).length = 13e-3
#vwire(i).x0 = -24.25e-3-w_rad/2
#vwire(i).width = w_rad
#vwire(i).z0 = -10e-3
#vwire(i).height = 3e-3
#vwire(i).current = I_in
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Central Lead Macrowire'
#vwire(i).yd = -13e-3
#vwire(i).length = 13e-3
#vwire(i).x0 = 24.25e-3-w_rad/2
#vwire(i).width = w_rad
#vwire(i).z0 = -10e-3
#vwire(i).height = 3e-3
#vwire(i).current = -I_in
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Left Central Thick Lead Microwire'
#vwire(i).yd = -11e-3
#vwire(i).length = 11.5e-3
#vwire(i).x0 = -12.75e-3
#vwire(i).width = w_micro_thlead
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = I_micro_trap
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Central Thick Lead Microwire'
#vwire(i).yd = -11e-3
#vwire(i).length = 11.5e-3
#vwire(i).x0 = 11.75e-3
#vwire(i).width = w_micro_thlead
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = -I_micro_trap
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Left Arm Microwire'
#vwire(i).yd = -l_arms
#vwire(i).length = l_arms-(w_micro/2 + sp)
#vwire(i).x0 = -l_med/2 - w_micro/2
#vwire(i).width = w_micro
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = I_micro_arm
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Left Arm Thick Lead Microwire'
#vwire(i).yd = -13e-3
#vwire(i).length = 12.5e-3
#vwire(i).x0 = -11.75e-3
#vwire(i).width = w_micro_thlead
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = -I_micro_arm
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Left Arm Thick Return Microwire'
#vwire(i).yd = -16e-3
#vwire(i).length = 12e-3
#vwire(i).x0 = --10e-3
#vwire(i).width = w_micro_thlead
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = I_micro_arm
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Arm Microwire'
#vwire(i).yd = w_micro/2 + sp
#vwire(i).length = l_arms-(w_micro/2 + sp)
#vwire(i).x0 = l_med/2 - w_micro/2
#vwire(i).width = w_micro
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = I_micro_arm
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Arm Thick Lead Microwire'
#vwire(i).yd = -13e-3
#vwire(i).length = 12.5e-3
#vwire(i).x0 = 12.75e-3
#vwire(i).width = w_micro_thlead
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = I_micro_arm
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Right Arm Thick Return Microwire'
#vwire(i).yd = -6e-3
#vwire(i).length = 10e-3
#vwire(i).x0 = 15e-3
#vwire(i).width = w_micro_thlead
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = -I_micro_arm
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1
#
#vwire(i).name = 'Dimple Microwire'
#vwire(i).yd = w_micro/2 + sp
#vwire(i).length = l_arms-(w_micro/2 + sp)
#vwire(i).x0 = -w_micro/2
#vwire(i).width = w_micro
#vwire(i).z0 = chip_height
#vwire(i).height = h_micro
#vwire(i).current = -I_micro_dimple
#vwire(i).subwires = n
#n_vwires = n_vwires + 1
#n_vsubwires = n_vsubwires + vwire(i).subwires^2
#i = i + 1

vwires.append(VWire( 'Left Axial Bias Lead Macrowire',  20e-3,  w_ax,  3e-3,  I_ax,  n,  -a_ax/2-w_ax/2,  -25e-3,  -3.1e-3))

vwires.append(VWire( 'Right Axial Bias Macrowire',  l_ax,  w_ax,  h_ax,  I_ax,  n,  a_ax/2-w_ax/2,  -l_ax/2,  -sub - h_ax/2))

vwires.append(VWire( 'Right Axial Bias Lead Macrowire',  20e-3,  w_ax,  3e-3,  I_ax,  n,  a_ax/2-w_ax/2,  -25e-3,  -3.1e-3))

vwires.append(VWire( 'Axial Dimple Macrowire',  l_ax,  w_dimple,  h_dimple,  I_dimple,  n,  -w_dimple/2,  -l_ax/2,  -sub - h_dimple/2))

vwires.append(VWire( 'Axial Dimple Lead Macrowire',  20e-3,  w_dimple,  3e-3,  I_dimple,  n,  -w_dimple/2,  -25e-3,  -3.1e-3))

vwires.append(VWire( 'Left Bias Lead Macrowire',  2.75e-3,  w_rad,  h_ax,  -I_out,  n,  -24.25e-3-w_rad/2,  -6e-3,  -sub-h_ax/2))

vwires.append(VWire( 'Right Bias Lead Macrowire',  2.75e-3,  w_rad,  h_ax,  I_out,  n,  24.25e-3-w_rad/2,  -6e-3,  -sub-h_ax/2))

vwires.append(VWire( 'Left Central Lead Macrowire',  13e-3,  w_rad,  3e-3,  I_in,  n,  -24.25e-3-w_rad/2,  -13e-3,  -10e-3))

vwires.append(VWire( 'Right Central Lead Macrowire',  13e-3,  w_rad,  3e-3,  -I_in,  n,  24.25e-3-w_rad/2,  -13e-3,  -10e-3))

vwires.append(VWire( 'Left Central Thick Lead Microwire',  11.5e-3,  w_micro_thlead,  h_micro,  I_micro_trap,  n,  -12.75e-3,  -11e-3,  chip_height))

vwires.append(VWire( 'Right Central Thick Lead Microwire',  11.5e-3,  w_micro_thlead,  h_micro,  -I_micro_trap,  n,  11.75e-3,  -11e-3,  chip_height))

vwires.append(VWire( 'Left Arm Microwire',  l_arms-(w_micro/2 + sp),  w_micro,  h_micro,  I_micro_arm,  n,  -l_med/2 - w_micro/2,  -l_arms,  chip_height))

vwires.append(VWire( 'Left Arm Thick Lead Microwire',  12.5e-3,  w_micro_thlead,  h_micro,  -I_micro_arm,  n,  -11.75e-3,  -13e-3,  chip_height))

vwires.append(VWire( 'Left Arm Thick Return Microwire',  12e-3,  w_micro_thlead,  h_micro,  I_micro_arm,  n,  --10e-3,  -16e-3,  chip_height))

vwires.append(VWire( 'Right Arm Microwire',  l_arms-(w_micro/2 + sp),  w_micro,  h_micro,  I_micro_arm,  n,  l_med/2 - w_micro/2,  w_micro/2 + sp,  chip_height))

vwires.append(VWire( 'Right Arm Thick Lead Microwire',  12.5e-3,  w_micro_thlead,  h_micro,  I_micro_arm,  n,  12.75e-3,  -13e-3,  chip_height))

vwires.append(VWire( 'Right Arm Thick Return Microwire',  10e-3,  w_micro_thlead,  h_micro,  -I_micro_arm,  n,  15e-3,  -6e-3,  chip_height))

vwires.append(VWire( 'Dimple Microwire',  l_arms-(w_micro/2 + sp),  w_micro,  h_micro,  -I_micro_dimple,  n,  -w_micro/2,  w_micro/2 + sp,  chip_height))


# Normal Wires
n_nwires = 0
n_nsubwires = 0
i = 1

# nwire(i).name = 'Left Axial Lead Macrowire'
# nwire(i).zd = -15e-3
# nwire(i).length =13.7e-3
# nwire(i).x0 = -8.75e-3
# nwire(i).width = 3e-3
# nwire(i).y0 = 4e-3
# nwire(i).breadth = 1e-3
# nwire(i).current = -I_ax
# nwire(i).subwires = n
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1
# 
# nwire(i).name = 'Right Axial Lead Macrowire'
# nwire(i).zd = -15e-3
# nwire(i).length =13.7e-3
# nwire(i).x0 = 5.75e-3
# nwire(i).width = 3e-3
# nwire(i).y0 = 4e-3
# nwire(i).breadth = 1e-3
# nwire(i).current = -I_ax
# nwire(i).subwires = n
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1
# 
# nwire(i).name = 'Left Axial Lead Rod'
# nwire(i).zd = -40e-3
# nwire(i).length =40e-3
# nwire(i).x0 = -a_ax/2
# nwire(i).width = 0
# nwire(i).y0 = -30e-3
# nwire(i).breadth = 0
# nwire(i).current = I_ax
# nwire(i).subwires = 1
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1
# 
# nwire(i).name = 'Right Axial Lead Rod'
# nwire(i).zd = -40e-3
# nwire(i).length =40e-3
# nwire(i).x0 = a_ax/2
# nwire(i).width = 0
# nwire(i).y0 = -30e-3
# nwire(i).breadth = 0
# nwire(i).current = I_ax
# nwire(i).subwires = 1
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1
# 
# nwire(i).name = 'Dimple Lead Rod'
# nwire(i).zd = -40e-3
# nwire(i).length =40e-3
# nwire(i).x0 = 0
# nwire(i).width = 0
# nwire(i).y0 = -30e-3
# nwire(i).breadth = 0
# nwire(i).current = I_dimple
# nwire(i).subwires = 1
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1
# 
#nwire(i).name = 'Left Upper Bias Lead Rod'
#nwire(i).zd = -40e-2
#nwire(i).length =40e-2
#nwire(i).x0 = -40e-3
#nwire(i).width = 0
#nwire(i).y0 = 0
#nwire(i).breadth = 0
#nwire(i).current = -I_out
#nwire(i).subwires = 1
#n_nwires = n_nwires + 1
#n_nsubwires = n_nsubwires + nwire(i).subwires^2
#i = i + 1
#
#nwire(i).name = 'Right Upper Bias Lead Rod'
#nwire(i).zd = -40e-2
#nwire(i).length =40e-2
#nwire(i).x0 = 40e-3
#nwire(i).width = 0
#nwire(i).y0 = 0
#nwire(i).breadth = 0
#nwire(i).current = I_out
#nwire(i).subwires = 1
#n_nwires = n_nwires + 1
#n_nsubwires = n_nsubwires + nwire(i).subwires^2
#i = i + 1
#
#nwire(i).name = 'Left Lower Bias Lead Rod'
#nwire(i).zd = -40e-2
#nwire(i).length =390e-3
#nwire(i).x0 = -30e-3
#nwire(i).width = 0
#nwire(i).y0 = 0
#nwire(i).breadth = 0
#nwire(i).current = -I_out
#nwire(i).subwires = 1
#n_nwires = n_nwires + 1
#n_nsubwires = n_nsubwires + nwire(i).subwires^2
#i = i + 1
#
#nwire(i).name = 'Right Lower Bias Lead Rod'
#nwire(i).zd = -40e-2
#nwire(i).length =390e-3
#nwire(i).x0 = 30e-3
#nwire(i).width = 0
#nwire(i).y0 = 0
#nwire(i).breadth = 0
#nwire(i).current = I_out
#nwire(i).subwires = 1
#n_nwires = n_nwires + 1
#n_nsubwires = n_nsubwires + nwire(i).subwires^2
#i = i + 1

nwires.append(NWire( 'Left Upper Bias Lead Rod', 40e-2,  0,  0,  -I_out,  1,  -40e-3,  0,  -40e-2))

nwires.append(NWire( 'Right Upper Bias Lead Rod', 40e-2,  0,  0,  I_out,  1,  40e-3,  0,  -40e-2))

nwires.append(NWire( 'Left Lower Bias Lead Rod', 390e-3,  0,  0,  -I_out,  1,  -30e-3,  0,  -40e-2))

nwires.append(NWire( 'Right Lower Bias Lead Rod', 390e-3,  0,  0,  I_out,  1,  30e-3,  0,  -40e-2))



# 
# nwire(i).name = 'Left Central Lead Rod'
# nwire(i).zd = -40e-2
# nwire(i).length =390e-3
# nwire(i).x0 = -30e-3
# nwire(i).width = 0
# nwire(i).y0 = -20e-3
# nwire(i).breadth = 0
# nwire(i).current = I_in
# nwire(i).subwires = 1
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1
# 
# nwire(i).name = 'Right Central Lead Rod'
# nwire(i).zd = -40e-2
# nwire(i).length =390e-3
# nwire(i).x0 = 30e-3
# nwire(i).width = 0
# nwire(i).y0 = -20e-3
# nwire(i).breadth = 0
# nwire(i).current = -I_in
# nwire(i).subwires = 1
# n_nwires = n_nwires + 1
# n_nsubwires = n_nsubwires + nwire(i).subwires^2
# i = i + 1

## Vector Generation
# Horizontal
fin_horz_params = zeros(5,n_hsubwires)
XL = []
XR = []
Y0 = []
Z0 = []
I = []

#for ii = 1:n_hwires
for ii in range(n_hwires):
    nn = hwire(ii).subwires
    XL = [XL, hwire(ii).xl*ones(1,nn^2)]
    XR = [XR, (hwire(ii).xl + hwire(ii).length)*ones(1,nn^2)]
    Y0 = [Y0, repmat(linspace(hwire(ii).y0, (hwire(ii).y0 + hwire(ii).width), nn),1,nn)]
    z_values = linspace(hwire(ii).z0, (hwire(ii).z0 + hwire(ii).height),nn)
    Z_vector = []
#    for jj = 1:hwire(ii).subwires
    for jj in range(hwire(ii).subwires):
        Z_vector = [Z_vector, z_values(jj)*ones(1,nn)]
    Z0 = [Z0, Z_vector]
    I = [I, hwire(ii).current/nn^2 * ones(1,nn^2)]

fin_horz_params(1,:) = XL
fin_horz_params(2,:) = XR
fin_horz_params(3,:) = Y0
fin_horz_params(4,:) = Z0
fin_horz_params(5,:) = I


# Vertical
fin_vert_params = zeros(5,n_vsubwires)
YD = []
YU = []
X0 = []
Z0 = []
I = []

#for ii = 1:n_vwires
for ii in range(n_vwires):
    nn = vwire(ii).subwires
    YD = [YD, vwire(ii).yd*ones(1,nn^2)]
    YU = [YU, (vwire(ii).yd + vwire(ii).length)*ones(1,nn^2)]
    X0 = [X0, repmat(linspace(vwire(ii).x0, (vwire(ii).x0 + vwire(ii).width), nn),1,nn)]
    z_values = linspace(vwire(ii).z0, (vwire(ii).z0 + vwire(ii).height),nn)
    Z_vector = []
#    for jj = 1:vwire(ii).subwires
    for jj in range(vwire(ii).subwires):
        Z_vector = [Z_vector, z_values(jj)*ones(1,nn)]
    Z0 = [Z0, Z_vector]
    I = [I, vwire(ii).current/nn^2 * ones(1,nn^2)]

fin_vert_params(1,:) = YD
fin_vert_params(2,:) = YU
fin_vert_params(3,:) = X0
fin_vert_params(4,:) = Z0
fin_vert_params(5,:) = I


# Normal
fin_norm_params = zeros(5,n_nsubwires)
ZD = []
ZU = []
X0 = []
Y0 = []
I = []

#for ii = 1:n_nwires
for ii in range(n_nwires):
    nn = nwire(ii).subwires
    ZD = [ZD, nwire(ii).zd*ones(1,nn^2)]
    ZU = [ZU, (nwire(ii).zd + nwire(ii).length)*ones(1,nn^2)]
    X0 = [X0, repmat(linspace(nwire(ii).x0, (nwire(ii).x0 + nwire(ii).width), nn),1,nn)]
    y_values = linspace(nwire(ii).y0, (nwire(ii).y0 + nwire(ii).breadth),nn)
    Y_vector = []
#    for jj = 1:nwire(ii).subwires
    for jj in range(nwire(ii).subwires):
        Y_vector = [Y_vector, y_values(jj)*ones(1,nn)]
    Y0 = [Y0, Y_vector]
    I = [I, nwire(ii).current/nn^2 * ones(1,nn^2)]

fin_norm_params(1,:) = ZD
fin_norm_params(2,:) = ZU
fin_norm_params(3,:) = X0
fin_norm_params(4,:) = Y0
fin_norm_params(5,:) = I
toc