# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:30:17 2013

@author: Will
"""

import Window
import AtomImage

class ImagingSystem:
    def __init__(self):
        pass
    def image(self, atom_image):
        initial_window = atom_image.get_window()
        imaged_window = initial_window #placeholder
        imaged_image = AtomImage.AtomImage(atom_image.get_image_arr(), 
                                           atom_image.get_imaging_beam(), 
                                           imaged_window)
        return imaged_image #placeholder