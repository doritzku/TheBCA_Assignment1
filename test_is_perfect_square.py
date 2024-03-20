#The following code is a unit test for is_perfect_square.py
#written by Viren Hemrajani, 500089749.

import unittest
from is_perfect_square import is_perfect_square

class TestIsPerfectSquare(unittest.TestCase):
    """Unit tests for the is_perfect_square function."""

    def test_perfect_squares(self):
        """Test perfect squares."""
        # Test perfect squares (0, 1, 4, 9, 16, 25, 36)
        self.assertTrue(is_perfect_square(0))
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertTrue(is_perfect_square(25))
        self.assertTrue(is_perfect_square(36))

    def test_non_perfect_squares(self):
        """Test non-perfect squares."""
        # Test non-perfect squares (2, 3, 5, 6, 7, 8)
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(6))
        self.assertFalse(is_perfect_square(7))
        self.assertFalse(is_perfect_square(8))

    def test_negative_number(self):
        """Test negative number."""
        # Test negative numbers
        self.assertFalse(is_perfect_square(-1))
        self.assertFalse(is_perfect_square(-4))
        self.assertFalse(is_perfect_square(-9))

if __name__ == "__main__":
    unittest.main()

