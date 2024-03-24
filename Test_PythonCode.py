import unittest
from PythonCode import armstrong_500089748

# Test code for Armstrong 500089748
class Test_armstrong_500089748(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertEqual(armstrong_500089748(153), "Armstrong Number")  # Testing Armstrong number 153
        self.assertEqual(armstrong_500089748(370), "Armstrong Number")  # Testing Armstrong number 370
        self.assertEqual(armstrong_500089748(9474), "Armstrong Number") # Testing Armstrong number 9474

    def test_not_armstrong_number(self):
        self.assertEqual(armstrong_500089748(123), "Not an Armstrong Number")  # Testing non-Armstrong number 123
        self.assertEqual(armstrong_500089748(12345), "Not an Armstrong Number")  # Testing non-Armstrong number 12345

    def test_single_digit_number(self):
        self.assertEqual(armstrong_500089748(5), "Armstrong Number")  # Testing single digit Armstrong number 5
        self.assertEqual(armstrong_500089748(9), "Armstrong Number")  # Testing single digit Armstrong number 9

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):  # Testing TypeError for non-integer input
            armstrong_500089748("hello")

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):  # Testing ValueError for negative input
            armstrong_500089748(-153)

# ...

if __name__ == '__main__':
    unittest.main()



