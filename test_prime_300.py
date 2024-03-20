import unittest
from PythonCode import prime_300

class TestPrime300(unittest.TestCase):
    """Unit tests for the prime_300 function."""

    def test_prime_number(self):
        """Test prime numbers."""
        self.assertEqual(prime_300(2), "Prime Number")
        self.assertEqual(prime_300(3), "Prime Number")
        self.assertEqual(prime_300(5), "Prime Number")
        self.assertEqual(prime_300(7), "Prime Number")

    def test_non_prime_number(self):
        """Test non-prime numbers."""
        self.assertEqual(prime_300(4), "Not a Prime Number")
        self.assertEqual(prime_300(6), "Not a Prime Number")
        self.assertEqual(prime_300(8), "Not a Prime Number")

    def test_invalid_input(self):
        """Test invalid input."""
        with self.assertRaises(TypeError):
            prime_300("abc")
        with self.assertRaises(ValueError):
            prime_300(0)

if __name__ == "__main__":
    unittest.main()
#########################################################################
