# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:35:49 2013

@author: Will
"""

from collections import namedtuple
import numpy as np

wmin = -500 #um
wmax = 500 #um
wnum = 100

wmin = wmin * 1e-6 #m
wmax = wmax * 1e-6 #m



Window = namedtuple('Window', ['min','max','num_cells', 'window'])

window = Window(wmin, wmax, wnum, np.linspace(wmin, wmax, wnum))

#class Window():
#    def __init__(self):
#        pass