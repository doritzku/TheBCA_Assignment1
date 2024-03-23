'''
This is a test code for is_fibonacci.py using the unit test module
Written by Ankur Kumar 
Sap id: 500090333
Course: BCA (CSF)
'''

import unittest
from is_fibonacci import is_fibonacci_number

def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    for i in range(2, n + 1):  # Corrected range
        next_number = sequence[i - 1] + sequence[i - 2]  # Calculate the next Fibonacci number
        sequence.append(next_number)
    return sequence



class TestFibonacciSequence(unittest.TestCase):
    def test_fibonacci_sequence(self):
        # Test Fibonacci sequence for the first 10 terms
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_sequence(10), expected_sequence, "First 10 terms of Fibonacci sequence mismatch")

        # Test Fibonacci sequence for 0 terms
        self.assertEqual(fibonacci_sequence(0), [], "Fibonacci sequence for 0 terms mismatch")

        # Test Fibonacci sequence for 1 term
        self.assertEqual(fibonacci_sequence(1), [0], "Fibonacci sequence for 1 term mismatch")

        # Test Fibonacci sequence for 2 terms
        self.assertEqual(fibonacci_sequence(2), [0, 1], "Fibonacci sequence for 2 terms mismatch")

        # Test Fibonacci sequence for negative number of terms
        self.assertEqual(fibonacci_sequence(-5), [], "Fibonacci sequence for negative terms mismatch")

if __name__ == '__main__':
    unittest.main()
