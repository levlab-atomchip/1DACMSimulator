# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:29:28 2013

@author: Will
"""

from Window import Window
import numpy as np

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
    def __init__(self, image_arr, CCD):
        wmin = -0.5 * CCD.length
        wmax = 0.5 * CCD.length
        wnum = CCD.num_pixel
        Image.__init__(self, image_arr, Window(wmin, wmax, wnum, 
                                         np.linspace(wmin, wmax, wnum)))
        self.CCD = CCD
    def get_analog(self, analog_resolution):
        wmin = -0.5 * self.CCD.length
        wmax = 0.5 * self.CCD.length
        window = np.arange(wmin, wmax, analog_resolution)
        analog_window = Window(wmin, wmax, len(window), window)
        pixel = 0
        analog_arr = []
        for cell in analog_window.window:
            if (self.window.window[pixel] + self.CCD.pixel_size) > cell:
                analog_arr.append(self.image_arr[pixel])
            else:
                pixel += 1
                analog_arr.append(self.image_arr[pixel])
        analog_image = Image(analog_arr, analog_window)
        return analog_image
    def get_CCD(self):
        return self.CCD
        