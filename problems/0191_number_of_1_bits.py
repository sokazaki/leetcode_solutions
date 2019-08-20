# O(N) Solution with Built-In Method

import unittest


def hammingWeight(n):

    return bin(n).count('1')


class Test(unittest.TestCase):

    def test_hammingWeight(self):
        self.assertEqual(hammingWeight(2**32), 1)
        self.assertEqual(hammingWeight(2**32-1), 32)
        self.assertEqual(hammingWeight(16), 1)
        self.assertEqual(hammingWeight(15), 4)
        self.assertEqual(hammingWeight(0), 0)

if __name__ == "__main__":

    unittest.main()
