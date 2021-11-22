from sum import sum2
import unittest

#def sum2(a):
#    return a+2

class Testsum2(unittest.TestCase):

    def test1(self):
        result = sum2(1)

        self.assertEqual(result, 3)

    def test2(self):
        result = sum2(2)

        self.assertEqual(result, 4)

    def test3(self):
        self.assertRaises(ValueError, sum2, -1)

unittest.main()
