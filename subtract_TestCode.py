import unittest
from subtract import subtract_values

class TestSubtractFunction(unittest.TestCase):
    def test_subtract_numeric_values(self):
        # Test subtracting two positive numbers
        result = subtract_values(10, 5)
        self.assertEqual(result, 5)

        # Test subtracting two negative numbers
        result = subtract_values(-10, -5)
        self.assertEqual(result, -5)

        # Test subtracting a positive number from zero
        result = subtract_values(0, 5)
        self.assertEqual(result, -5)

        # Test subtracting zero from a positive number
        result = subtract_values(10, 0)
        self.assertEqual(result, 10)

        # Test subtracting zero from zero
        result = subtract_values(0, 0)
        self.assertEqual(result, 0)

    def test_subtract_non_numeric_values(self):
        # Test subtracting a non-numeric value from a numeric value
        result = subtract_values("10", 5)
        self.assertEqual(result, "Error: Both inputs must be numeric values.")

        # Test subtracting a numeric value from a non-numeric value
        result = subtract_values(10, "5")
        self.assertEqual(result, "Error: Both inputs must be numeric values.")

        # Test subtracting two non-numeric values
        result = subtract_values("10", "5")
        self.assertEqual(result, "Error: Both inputs must be numeric values.")

    def test_subtract_other_data_types(self):
        # Test subtracting floating point numbers
        result = subtract_values(10.5, 5.2)
        self.assertAlmostEqual(result, 5.3)

        # Test subtracting complex numbers
        result = subtract_values(3+4j, 1+2j)
        self.assertEqual(result, (2+2j))

        # Test subtracting lists
        result = subtract_values([1, 2, 3], [1, 1, 1])
        self.assertEqual(result, "Error: Both inputs must be numeric values.")

if __name__ == '__main__':
    unittest.main()