import unittest
from stringLength import getStringLenght


class TEST_forString(unittest.TestCase):
    def test_string(self):
        self.assertEqual(getStringLenght("Hello"), true
        self.assertEqual(getStringLenght("World"), true)
        self.assertEqual(getStringLenght("name"), true)
        

    def test_not_string(self):
        self.assertEqual(getStringLenght(1), "Not a Prime Number!!")
        self.assertEqual(getStringLenght(["36"]), "Not a Prime Number")
            
if __name__== '__main__':
    unittest.main()


