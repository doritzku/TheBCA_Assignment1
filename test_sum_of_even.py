#written by Arpita Bhardwaj, 500089338

import unittest
from sum_of_even import sum_of_even

class TestSumOfEven(unittest.TestCase):
    """Unit tests for the sum_of_even function."""

    def test_sum_of_even(self):
        """Test sum of even numbers."""
        self.assertEqual(sum_of_even(0), 0)
        self.assertEqual(sum_of_even(1), 0)
        self.assertEqual(sum_of_even(2), 2)
        self.assertEqual(sum_of_even(5), 6)
        self.assertEqual(sum_of_even(10), 30)
        self.assertEqual(sum_of_even(20), 110)

    def test_negative_input(self):
        """Test negative input."""
        with self.assertRaises(ValueError):
            sum_of_even(-1)

if __name__ == "__main__":
    unittest.main()

