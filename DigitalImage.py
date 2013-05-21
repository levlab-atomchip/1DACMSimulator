# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:33:44 2013

@author: Will
"""

from Window import window

class DigitalImage:
    def __init__(self, image_arr, CCD):
        self.image_arr = image_arr
        self.CCD = CCD
    def get_analog(self):
        pass