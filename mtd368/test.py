# test case

import unittest
from unittest import TestCase
import numpy as np
import numpy.testing as npt
import array
from array import arraybuilder, twoDArray, thedivider, arraymath, mandelbrot

"""test functions in array.py"""

class array_unittest(unittest.TestCase):

    def setUp(self):
        pass

    def test_twoDArray(self):
        x = np.array([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
        npt.assert_array_equal(twoDArray()[0], x) # accessing the first returned value from the function.

    def test_thedivider(self):
        x = np.array([[0.,0.2,0.2,0.2,0.2,],[5.,1.2,0.7,0.5,0.45],[10.,2.2,1.2,0.8,0.7],[15.,3.2,1.7,1.2,0.95],[20.,4.2,2.2,1.5,1.2]])
        npt.assert_almost_equal(thedivider(), x, decimal=1)

if __name__ == '__main__':
    unittest.main()