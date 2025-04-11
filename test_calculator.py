#Brandon Alvarez Repo - Partner 1 - https://github.com/Brandon-Alvarez-03/lab10-BA-JR
#BAlvarez Github Link and UF Email: https://github.com/Brandon-Alvarez-03
#brandon.alvarez@ufl.edu

#Jonathan Reyes Repo - Partner 2
#JReyes Github Link and UF Email: jreyes2@ufl.edu, https://github.com/nahtanoJ-dot-exe


#test_calculator.py
#- Unit tests for calculator.py

# https://github.com/Brandon-Alvarez-03/lab10-BA-JR
# Partner 1: Brandon Andrew Alvarez
# Partner 2: Jonathan Reyes


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, -3), 0)
        self.assertEqual(add(4, 0), 4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(7, -2), 9)
        self.assertEqual(subtract(3, 0), 3)
    # ##########################

    ######## Partner 1
    # Partner 1 responsibilities
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(4, -8), -2)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
             divide(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3, 9), 2.0)
        self.assertEqual(logarithm(2, 8), 3.0)
        self.assertEqual(logarithm(4, 256), 4.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()