# -*- coding: utf-8 -*-
"""
Created on Fri Jun 07 21:39:55 2013

@author: Will
"""

import numpy as np
import matplotlib.pyplot as plt
from math import pi

class Slab():
    def __init__(self, x_l, y_l, th, rez):
        self.x_l = x_l
        self.y_l = y_l
        self.th = th
        self.rez = rez
        self.x = np.arange(-0.5*self.x_l, 0.5*self.x_l, rez)
        self.y = np.arange(-0.5 * self.y_l, 0.5 * self.y_l, self.rez)
        self.X, self.Y = np.meshgrid(self.x, self.y)

class CurrentSlab():
    def __init__(self, slab, J_fn = None, theta_fn = None):
        self.delx = slab.rez
        self.th = slab.th
        self.X = slab.X
        self.Y = slab.Y
        self.theta = theta_fn(self.X, self.Y)
        self.J = J_fn(self.X, self.Y)
        self.dx = self.delx * np.cos(self.theta)
        self.dy = self.delx * np.sin(self.theta)
        
    def get_delx(self):
        return self.delx
    def get_th(self):
        return self.th
    def get_Y(self):
        return self.Y
    def get_X(self):
        return self.X
    def get_dx(self):
        return self.dx
    def get_dy(self):
        return self.dy
    def get_J(self):
        return self.J
    def plot_J(self):
        plt.contourf(self.X, self.Y,self.J)
        plt.colorbar()
#        scale = 0.1
#        plt.quiver(self.X, self.Y, scale*self.J*np.cos(self.theta), scale*self.J*np.sin(self.theta))
        plt.show()
        plt.contourf(self.X, self.Y, self.theta)
        plt.colorbar()
        plt.show()
    def rotate90(self):
        self.J = np.rot90(self.J)
        self.theta = (np.rot90(self.theta) - 0.5*pi) * (self.J > 0)