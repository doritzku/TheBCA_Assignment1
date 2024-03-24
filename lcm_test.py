#written by Namra Tyagi, 500091016

import unittest
from lcm import lcm

class TestLCM(unittest.TestCase):
    """Unit tests for the lcm function."""

    def test_lcm(self):
        """Test LCM."""
        self.assertEqual(lcm(3, 5), 15)
        self.assertEqual(lcm(7, 9), 63)
        self.assertEqual(lcm(15, 20), 60)
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(24, 36), 72)

    def test_large_numbers(self):
        """Test LCM with large numbers."""
        self.assertEqual(lcm(99999, 999999), 99998900001)
        self.assertEqual(lcm(123456789, 987654321), 3854883439000009)

    def test_zero_input(self):
        """Test LCM with zero input."""
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(7, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

if __name__ == "__main__":
    unittest.main()

