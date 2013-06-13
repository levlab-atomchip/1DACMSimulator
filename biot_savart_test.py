# -*- coding: utf-8 -*-
"""
Created on Fri Jun 07 21:39:28 2013

@author: Will
"""

from biot_savart import *
from CurrentSlab import *
from math import pi
from Window import Window
import numpy as np
from acmconstants import MU_0
import matplotlib.pyplot as plt

y_0 = 0
z_0 = 0.1
slab = Slab(1, 10, 1e-3, 1e-2)

def J_perp_wire(xx, yy):
    J = 1
    zz1 = xx < 2e-3
    zz2 = xx > -2e-3
    return np.logical_and(zz1, zz2)
    
def theta_perp_wire(xx, yy):
    zz = 0.5 * pi * np.ones(xx.shape)
    return zz
    
window = Window(-0.1, 0.1, 100)    

current_slab = CurrentSlab(slab, J_perp_wire, theta_perp_wire)

B = biot_savart(window, y_0, z_0, current_slab)

B.plot_mag()

prefactor = MU_0 * 1e-5 * 0.5 / pi
r = np.sqrt(window.window**2 + y_0**2 + z_0**2)
B_inf = prefactor / r
plt.plot(window.window, B_inf)
plt.show()
Bratio = B_inf / B.get_mag()
plt.plot(window.window, Bratio)
plt.show()