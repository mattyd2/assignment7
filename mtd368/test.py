# test case

import unittest
from unittest import TestCase
import numpy as np
import numpy.testing as npt
import array_module
from array_module import arraybuilder, twoDArray, thedivider, arraymath

"""test functions in array.py"""

class array_unittest(unittest.TestCase):

    def setUp(self):
        pass

    def test_twoDArray1(self):
        question1 = np.array([[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14], [5, 10, 15]])
        npt.assert_array_equal(twoDArray()[0], question1) # accessing the first returned value from the function.

    def test_twoDArray2(self):
        question1a = np.array([[2,7,12],[4,9,14]])
        npt.assert_array_equal(twoDArray()[1], question1a) # accessing the second returned value from the function.

    def test_twoDArray3(self):
        question1b = np.array([[6],[7],[8],[9],[10]])
        npt.assert_array_equal(twoDArray()[2], question1b) # accessing the first returned value from the function.
    
    def test_twoDArray4(self):
        question1c = np.array([[2,7,12],[3,8,13],[4,9,14]])
        npt.assert_array_equal(twoDArray()[3], question1c) # accessing the first returned value from the function.

    def test_twoDArray5(self):
        question1d = np.array([6,7,8,4,9,5,10])
        npt.assert_array_equal(twoDArray()[4], question1d) # accessing the first returned value from the function.

    def test_thedivider(self):
        x = np.array([[0.,0.2,0.2,0.2,0.2,],[5.,1.2,0.7,0.5,0.45],[10.,2.2,1.2,0.8,0.7],[15.,3.2,1.7,1.2,0.95],[20.,4.2,2.2,1.5,1.2]])
        npt.assert_almost_equal(thedivider(), x, decimal=1)

    # def test_thedivider(self):
    #     x = np.array([[0.,0.2,0.2,0.2,0.2,],[5.,1.2,0.7,0.5,0.45],[10.,2.2,1.2,0.8,0.7],[15.,3.2,1.7,1.2,0.95],[20.,4.2,2.2,1.5,1.2]])
    #     npt.assert_almost_equal(thedivider(), x, decimal=1)

if __name__ == '__main__':
    unittest.main()