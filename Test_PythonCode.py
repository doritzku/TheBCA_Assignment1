import unittest
from PythonCode import prime_300
from PythonCode import factorial

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
# test code for factorial
class Test_factorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)  # Testing factorial of 0
        self.assertEqual(factorial(1), 1)  # Testing factorial of 1
        self.assertEqual(factorial(2), 2)  # Testing factorial of 2
        self.assertEqual(factorial(3), 6)  # Testing factorial of 3
        self.assertEqual(factorial(4), 24)  # Testing factorial of 4

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):  # Testing TypeError for non-integer input
            factorial("hello")

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):  # Testing ValueError for negative input
            factorial(-7)

    def test_large_input(self):
        self.assertEqual(factorial(10), 3628800)  # Testing factorial of 10
            
if __name__== '__main__':
    unittest.main()


