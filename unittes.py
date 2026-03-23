from math_utils import *

import unittest


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-3,2), -1)
        self.assertEqual(add(2.9, 3), 5.9)

    def test_substract(self):
        self.assertEqual(substract(2,3), -1)
        self.assertEqual(substract(-3,2), -5)
        self.assertEqual(round(substract(2.9, 3), 5), -0.1)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(-3,2), -6)
        self.assertEqual(multiply(2.9, 3), 8.7)

    def test_divide(self):
        self.assertEqual(divide(3,2), 1.5)
        self.assertEqual(divide(-3,2), -1.5)
        
    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3,0)

    def test_type_raises(self):
        with self.assertRaises(TypeError):
            add(2, "2")

        with self.assertRaises(TypeError):
            substract(2, "2")

        with self.assertRaises(TypeError):
            multiply([], ())
        
        with self.assertRaises(TypeError):
            divide([], ())
    