#This is unit test function to test PythonCode.py, written by Viren Hemrajani, 500089749.

import unittest
from PythonCode import prime_300

class TestPrime300(unittest.TestCase):
    """Unit tests for the prime_300 function."""


#the below tests if the input is equal to prime number or not.
    def test_prime_number(self):
        """Test prime numbers."""
        self.assertEqual(prime_300(2), "Prime Number")
        self.assertEqual(prime_300(3), "Prime Number")
        self.assertEqual(prime_300(5), "Prime Number")
        self.assertEqual(prime_300(7), "Prime Number")


#the below tests if the input is not equal to a prime number or not.
    def test_non_prime_number(self):
        """Test non-prime numbers."""
        self.assertEqual(prime_300(4), "Not a Prime Number")
        self.assertEqual(prime_300(6), "Not a Prime Number")
        self.assertEqual(prime_300(8), "Not a Prime Number")


#the below tests if the input is an invalid input or not, i.e something that not an integer or 0.
    def test_invalid_input(self):
        """Test invalid input."""
        with self.assertRaises(TypeError):
            prime_300("abc")
        with self.assertRaises(ValueError):
            prime_300(0)

if __name__ == "__main__":
    unittest.main()

