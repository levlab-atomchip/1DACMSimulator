# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:25:57 2013

@author: Will
"""

import random
import unittest
import acwires

class TestWireFunctions(unittest.TestCase):

    def setUp(self):
        self.wirelength = 1000
        self.testdist = .1
        self.hwire = acwires.HWire('test hwire', self.wirelength, .001, .001, 1, 1, 0, 0, 0)

    def test_bfield(self):
        bfield = self.hwire.bfieldcalc(self.wirelength / 2, 0, self.testdist)
        assertAlmostEqual(bfield, )
if __name__ == '__main__':
    unittest.main()