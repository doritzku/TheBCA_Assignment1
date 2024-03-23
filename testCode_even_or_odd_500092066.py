import unittest

# Importing the function I want to test from the repository.

from CodeFile_even_or_odd_500092066 import even_or_odd_500092066

class Test_even_or_odd_500092066(unittest.TestCase):
    def test_even_number(self):

        # Testing if the function correcCtly identifies even numbers.

        result = even_or_odd_500092066(4)
        self.assertEqual(result, "Even")

    def test_odd_number(self):

        # Testing if the function correctly identifies odd numbers.

        result = even_or_odd_500092066(7)
        self.assertEqual(result, "Odd")

    def test_zero(self):

        # Testing if the function correctly identifies zero.

        result = even_or_odd_500092066(0)
        self.assertEqual(result, "Even")  # Zero is considered even for this test

if __name__ == '__main__':
    unittest.main()

