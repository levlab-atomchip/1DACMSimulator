# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:35:49 2013

@author: Will
"""

#from collections import namedtuple
import numpy as np

wmin = -50 #um
wmax = 50 #um
#wmin = -13 * 512
#wmax = 13 * 512
wnum = 2048

wmin = wmin * 1e-6 #m
wmax = wmax * 1e-6 #m



# Window = namedtuple('Window', ['min','max','num_cells', 'window'])

# window = Window(wmin, wmax, wnum, np.linspace(wmin, wmax, wnum))

class Window():
   def __init__(self, xmin, xmax, num_cells):
       self.xmin = xmin
       self.xmax = xmax
       self.num_cells = num_cells
       self.window = np.linspace(xmin, xmax, num_cells)
       self.cell_size = (self.xmax - self.xmin) / self.num_cells
	   
window = Window(wmin, wmax, wnum)