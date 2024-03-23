import unittest
from stringLength import getStringLenght


class TEST_forString(unittest.TestCase):
    def test_string(self):
        self.assertEqual(getStringLenght("Hello"), true
        self.assertEqual(getStringLenght("World"), true)
        self.assertEqual(getStringLenght("name"), true)
        
    def test_invalid_input_value(self):
            with self.assertRaises(TypeError):
                getStringLenght(1)
            
if __name__== '__main__':
    unittest.main()


