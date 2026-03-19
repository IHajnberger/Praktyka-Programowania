import unittest
from kalkulator import Add

class Test(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(" "), 0)
    def test_single(self):
        self.assertEqual(Add("1"), 1)
    def test_two(self):
        self.assertEqual(Add("1,2"), 3)
    def test_multiple(self):
        self.assertEqual(Add("1,2,3,4,5"), 15)
    def test_error(self):
        with self.assertRaises(ValueError):
            Add("b,\n")
    def test_separator(self):
        self.assertEqual(Add("1\n2,3"), 6)
    def test_seperror(self):
        with self.assertRaises(ValueError):
            Add("1,\n2,3\n")

if __name__ == '__main__':
    unittest.main()