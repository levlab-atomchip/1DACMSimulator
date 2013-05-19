# -*- coding: utf-8 -*-
"""
Created on Sat May 18 20:39:42 2013

@author: Will
"""
import unittest
import numpy as np
import Measurement

class TestMeasurementFunctions(unittest.TestCase):

    def setUp(self):
        self.test_values = np.random.normal(0,1,10)
        self.meas = Measurement.Measurement(np.mean(self.test_values), np.std(self.test_values, ddof = 1), len(self.test_values), "meters")

    def test_getval(self):
        # make sure the shuffled sequence does not lose any elements
        self.assertEqual(np.mean(self.test_values), self.meas.getval())

    def test_rescale(self):
        unscaled_val = self.meas.getval()
        self.meas.rescale(1000, "millimeters")
        self.assertEqual(1000*unscaled_val, self.meas.getval())
        self.assertEqual(self.meas.getunit(), "millimeters")
        

    def test_update(self):
        observed_val = np.random.normal(0,1)
        new_test_values = np.append(self.test_values, observed_val)
        self.meas.update(observed_val)
        self.assertAlmostEqual(self.meas.getval(), np.mean(new_test_values))
        self.assertAlmostEqual(self.meas.getunc(), np.std(new_test_values, ddof = 1))
        self.assertEqual(self.meas.getnum(), len(new_test_values))


if __name__ == '__main__':
    unittest.main()