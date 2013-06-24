# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:28:42 2013

Only good to 2%!!

@author: Will
"""

from biot_savart import *
from CurrentSlab import *
from math import pi
from Window import Window, Window_2D
import numpy as np
from acmconstants import MU_0
import matplotlib.pyplot as plt

rez = 1e-4
th = 5e-6

y_0 = 0
z_0 = 300e-6
slab_xl = 1e-2
slab_yl = 1e-2

slab = Slab(slab_xl, slab_yl, th, rez)

wire_center_x = 0
wire_center_y = 0
wire_width = 2e-4
wire_length = 10
wire_J = 1e10
wire_theta = 0.5*pi

wire_I = wire_J*th*wire_width
print 'Wire Current (A): %2.2f'%wire_I
trap_bias = MU_0*wire_I / (2*pi*z_0)

def wire_wrapper_val(x_0, y_0, w, l, val):
    return lambda xx, yy: val_wire(xx, yy, x_0, y_0, w, l, val)

def val_wire(xx, yy, x_0, y_0, w, l, val):
    zz1 = xx < (x_0 + 0.5*w)
    zz2 = xx >= (x_0 - 0.5*w)
    zz3 = yy < (y_0 + 0.5*l)
    zz4 = yy >= (y_0 - 0.5*l)
    return val * np.logical_and(np.logical_and(np.logical_and(zz1, zz2), zz3),zz4)
    
#def theta_perp_wire(xx, yy, x_0, y_0, w, l, theta):
#    zz = 0.5 * pi * np.ones(xx.shape)
#    return zz
    
def z_trap_J(xx, yy, w, J):
    arm1 = val_wire(xx, yy, -0.5*(slab_xl - w), -0.25*(slab_xl + w), w, 0.5*(slab_xl - w), J)
    arm2 = val_wire(xx, yy,  0.5*(slab_xl - w),  0.25*(slab_xl + w), w, 0.5*(slab_xl - w), J)
    cent = val_wire(xx, yy, 0, 0, slab_xl, w, J)
    return arm1 + arm2 + cent
    
def z_trap_theta(xx, yy, w):
    arm1 = val_wire(xx, yy, -0.5*(slab_xl - w), -0.25*(slab_xl + w), w, 0.5*(slab_xl - w), 0.5*pi)
    arm2 = val_wire(xx, yy,  0.5*(slab_xl - w),  0.25*(slab_xl + w), w, 0.5*(slab_xl - w), 0.5*pi)
    return (arm1 + arm2)
    
def z_trap_J_wrap(w, J):
    return lambda xx, yy: z_trap_J(xx, yy, w, J)
    
def z_trap_theta_wrap(w):
    return lambda xx, yy: z_trap_theta(xx, yy, w)

scale = 1
window = Window(-0.5*scale*slab_xl, 0.5*scale*slab_xl, 1000)
#window_2d = Window_2D(-0.5*scale*slab_xl, -0.5*scale*slab_yl, 
#                      0.5*scale*slab_xl, 0.5*scale*slab_yl,
#                      30,30)    

current_slab = CurrentSlab(slab, z_trap_J_wrap(wire_width, wire_J), z_trap_theta_wrap(wire_width))
#current_slab.rotate90()

B = biot_savart(window, y_0, z_0, current_slab)
#B = biot_savart_2D(window_2d, z_0, current_slab)
B.add_bias([0,trap_bias, 0])
print 'Bias Field (G): %2.2f'%(1e4*trap_bias)

B.plot_mag()

#prefactor = MU_0 * (wire_width * th * wire_J)  * 0.5 / pi
#r = np.sqrt(window.window**2 + y_0**2 + z_0**2)
#B_inf = prefactor / r
#plt.plot(window.window, B_inf)
plt.show()
#current_slab.plot_J()
#Bratio = B_inf / B.get_mag()
#plt.plot(window.window, Bratio - 1)
#plt.show()