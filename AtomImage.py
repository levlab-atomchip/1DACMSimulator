# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:29:28 2013

@author: Will
"""

class Image():
    def __init__(self, image_arr, window):
        self.image_arr = image_arr
        self.window = window
    def get_window(self):
        return self.window
    def get_image_arr(self):
        return self.image_arr

class AtomImage(Image):
    ''' 1D array of light intensity after imaging '''
    def __init__(self, intensity_array, imaging_beam, window):
        Image.__init__(self, intensity_array, window)
        self.imaging_beam = imaging_beam
    def get_imaging_beam(self):
        return self.imaging_beam
        
class DigitalImage(Image):
    def __init__(self, image_arr, CCD, window):
        Image.__init__(image_arr, window)
        self.image_arr = image_arr
        self.CCD = CCD
    def get_analog(self, analog_window):
        pass
    def get_CCD(self):
        return self.CCD
        