# -*- coding: utf-8 -*-
"""
Created on Fri Jun 07 22:31:28 2013

@author: Will
"""

import numpy as np
import matplotlib.pyplot as plt

class BField():
    def __init__(self, window):
        self.window = window.window
        self.Bx = np.zeros(self.window.shape)
        self.By = np.zeros(self.window.shape)
        self.Bz = np.zeros(self.window.shape)
    def set_field(self, x, vec):
        nearest_x_ind = np.argmin(np.absolute(self.window - x))
        self.Bx[nearest_x_ind] = vec[0]
        self.By[nearest_x_ind] = vec[1]
        self.Bz[nearest_x_ind] = vec[2]
    def plot_mag(self):
        B = np.sqrt(self.Bx**2 + self.By**2 + self.Bz**2)
        plt.plot(self.window, 1e4*B)
        plt.xlabel('X')
        plt.ylabel('Field (G)')
#        plt.show()
    def get_mag(self):
        B = np.sqrt(self.Bx**2 + self.By**2 + self.Bz**2)
        return B
    def add_bias(self, bias):
        for x in xrange(len(self.window)):
            self.Bx[x] += bias[0]
            self.By[x] += bias[1]
            self.Bz[x] += bias[2]