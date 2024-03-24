import unittest
from automorphic import automorphic_500089748


# Test code for Automorphic number
class TEST_automorphic_500089748(unittest.TestCase):
    def test_automorphic_number(self):
        self.assertTrue(automorphic_500089748(5))    # Testing Automorphic number 5
        self.assertTrue(automorphic_500089748(6))    # Testing Automorphic number 6
        self.assertTrue(automorphic_500089748(25))   # Testing Automorphic number 25
        self.assertTrue(automorphic_500089748(76))   # Testing Automorphic number 76

    def test_not_automorphic_number(self):
        self.assertFalse(automorphic_500089748(11))   # Testing non-Automorphic number 11
        self.assertFalse(automorphic_500089748(12))   # Testing non-Automorphic number 12
        self.assertFalse(automorphic_500089748(100))  # Testing non-Automorphic number 100

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):  # Testing TypeError for non-integer input
            automorphic_500089748("hello")

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):  # Testing ValueError for negative input
            automorphic_500089748(-5)

# ...

if __name__ == '__main__':
    unittest.main()
