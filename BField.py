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
        plt.plot(self.window, B)
#        plt.show()
    def get_mag(self):
        B = np.sqrt(self.Bx**2 + self.By**2 + self.Bz**2)
        return B
