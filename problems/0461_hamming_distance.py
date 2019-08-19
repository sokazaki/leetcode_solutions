# Simple Solution with Built-In Method

import unittest

def hammingDistance(x, y):

    return bin(x^y).count('1')

class Test(unittest.TestCase):

    def test_hammingDistance(self):
        self.assertEqual(hammingDistance(1, 4), 2)
        self.assertEqual(hammingDistance(1, 1), 0)
        self.assertEqual(hammingDistance(0, 2**30), 1)
        self.assertEqual(hammingDistance(2, 2**30), 2)
        self.assertEqual(hammingDistance(2**30-1, 2**30), 31)

if __name__ == "__main__":

    unittest.main()
