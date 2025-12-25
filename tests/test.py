import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from operations import square
from operations import add_binary
from operations import sqrt


class OperationsTestCase (unittest.TestCase):
    def test_square(self):
        res = square(2)
        self.assertEqual(res,4)
    def test_square_null(self):
        res = square(0)
        self.assertEqual(res,0)
    def test_square_float(self):
        res = square(1.7)
        self.assertEqual(res,2.89)
    def test_square_neg(self):
        res = square(-3)
        self.assertEqual(res,9)


    def test_bin(self):
        res = add_binary(2,3)
        self.assertEqual(res,"101")
    def test_bin_null(self):
        res = add_binary(0,0)
        self.assertEqual(res,"0")
    def test_bin_float(self):
        with self.assertRaises(TypeError):
            add_binary(2,3.4)
    def test_bin_neg(self):
        res = add_binary(-1,-2)
        self.assertEqual(res, "-11")

    def test_sqrt_even(self):
        res = sqrt(4, 2)
        self.assertEqual(res,2)
    def test_sqrt_pdd(self):
        res = sqrt(27,3)
        self.assertEqual(res,3)
    def test_sqrt_num_null(self):
        res = sqrt(0,3)
        self.assertEqual(res,0)
    def test_sqrt_n_null(self):
        with self.assertRaises(ZeroDivisionError):
            sqrt(2,0)
    def test_sqrt_num_float(self):
        res = sqrt(0.25,2)
        self.assertEqual(res,0.5)
    def test_sqrt_n_float(self):
        res = sqrt(3, 0.5)
        self.assertEqual(res,9)
    def test_sqrt_num_neg(self):
        with self.assertRaises(ValueError):
            sqrt(-4, 2)
    def test_sqrt_n_neg(self):
        res = sqrt(4, -2)
        self.assertEqual(res, 0.5)
   
