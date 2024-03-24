'''
This is a test code for factorial function using the unit test module
Written by Hardik Gupta
Sap id: 500089339
'''

import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_positive_numbers(self):
        self.assertEqual(factorial(0), 1)  # Testing factorial of 0
        self.assertEqual(factorial(1), 1)  # Testing factorial of 1
        self.assertEqual(factorial(5), 120)  # Testing factorial of 5

    def test_factorial_negative_numbers(self):
        with self.assertRaises(ValueError):  # Testing factorial of negative number
            factorial(-5)

    def test_large_factorial(self):
        self.assertEqual(factorial(10), 3628800)  # Testing factorial of a large number (10)


if __name__ == '__main__':
    unittest.main()
