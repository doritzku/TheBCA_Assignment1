import unittest
from TheBCA_Assignment1.Assignment1.reverse_string import reverse

class TestReverseString(unittest.TestCase):
    def test_regular_string(self):
        self.assertEqual(reverse("hello"), "olleh")  # Testing regular string

    def test_empty_string(self):
        self.assertEqual(reverse(""), "")  # Testing empty string

    def test_string_with_special_characters(self):
        self.assertEqual(reverse("!@#$%^&*"), "*&^%$#@!")  # Testing string with special characters

    def test_string_with_numbers(self):
        self.assertEqual(reverse("12345"), "54321")  # Testing string with numbers

    def test_string_with_spaces(self):
        self.assertEqual(reverse("hello world"), "dlrow olleh")  # Testing string with spaces

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):  # Testing TypeError for non-string input
            reverse(123)


if __name__ == '__main__':
    unittest.main()
