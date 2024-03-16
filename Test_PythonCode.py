import unittest
from PythonCode import prime_300


# test code for prime 300
class TEST_prime_300(unittest.TestCase):
    def test_prime_number(self):
        self.assertEqual(prime_300(2), "Prime Number")  # Testing prime number 2
        self.assertEqual(prime_300(3), "Prime Number")  # Testing prime number 3
        self.assertEqual(prime_300(5), "Prime Number")  # Testing prime number 5
        self.assertEqual(prime_300(7), "Prime Number")  # Testing prime number 7
        self.assertEqual(prime_300(11), "Prime Number")  # Testing prime number 11

    def test_not_prime_number(self):
        self.assertEqual(prime_300(1), "Not a Prime Number!!")  # Testing not prime number 1
        self.assertEqual(prime_300(4), "Not a Prime Number")   # Testing not prime number 4
        self.assertEqual(prime_300(6), "Not a Prime Number")   # Testing not prime number 6
        self.assertEqual(prime_300(9), "Not a Prime Number")   # Testing not prime number 9
        self.assertEqual(prime_300(15), "Not a Prime Number")  # Testing not prime number 15

    def test_large_prime_number(self):
        self.assertEqual(prime_300(104729), "Prime Number")  # Testing a large prime number

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):  # Testing TypeError for non-integer input
            prime_300("hello")

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):  # Testing ValueError for negative input
            prime_300(-7)

#...
            
if __name__== '__main__':
    unittest.main()


