# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:35:25 2013

@author: Will
"""

import numpy as np
import scipy as sp
import math

class Measurement:
    def __init__(self, 
                 value, 
                 uncertainty, 
                 number, 
                 unit, 
                 distribution = "Gaussian"):
        self.value = value
        self.uncertainty = uncertainty
        self.number = number
        self.unit = unit
        self.distribution = distribution
        
    def getval(self):
        return self.value
        
    def getunc(self):
        return self.uncertainty
        
    def getnum(self):
        return self.number
        
    def getunit(self):
        return self.unit
    
    def declare(self, 
                value, 
                uncertainty, 
                number):
        self.value = value
        self.uncertainty = uncertainty
        self.number = number
        
    def rescale(self, scaling_factor, new_unit):
        self.value = self.value * scaling_factor
        self.uncertainty = self.uncertainty * scaling_factor
        self.unit = new_unit
        
    def update(self, observed_value):
        self.number += 1
        self.value = (((self.number - 1) * self.value + observed_value) 
                    / (self.number))
        self.uncertainty = math.sqrt((((self.number - 1)*
                                        (self.number - 2)*
                                        self.uncertainty**2
                            + (self.number)*(observed_value - self.value)**2)
                            / (self.number - 1)**2))

        
    def sample(self):
        return np.random.normal(self.value, self.uncertainty)
        
    def conf_int(self, alpha):
        return sp.stats.norm.interval(alpha, self.value, self.uncertainty)
        
    