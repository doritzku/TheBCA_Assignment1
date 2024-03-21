'''
This is a test code for is_armstrong.py using the unit test module
Written by Sanya Mehta
Sap id: 500092051
'''

import unittest
from is_armstrong import is_armstrong


class TestArmstrong(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertTrue(is_armstrong(153))  # Testing armstrong number 153
        self.assertTrue(is_armstrong(371))  # Testing armstrong number 371
        self.assertTrue(is_armstrong(1634))  # Testing armstrong number 1634
       

    def test_not_armstrong_number(self):
        self.assertFalse(is_armstrong(245))  # Testing non armstrong number 245
        self.assertFalse(is_armstrong(469))   # Testing non armstrong number 469
        self.assertFalse(is_armstrong(6278))   # Testing non armstrong number 6278
        

    def test_large_armstrong_number(self):
        self.assertTrue(is_armstrong(9926315), "Armstrong Number")  # Testing a large armstrong number

    

            
if __name__== '__main__':
    unittest.main()