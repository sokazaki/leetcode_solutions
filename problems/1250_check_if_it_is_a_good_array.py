# O(N) Solution with Bézout's identity

import unittest
from math import gcd
from functools import reduce


def isGoodArray(nums):
    return True if reduce(gcd, nums) == 1 else False

class Test(unittest.TestCase):

    def test_isGoodArray(self):
        self.assertEqual(isGoodArray([12,5,7,23]), True)
        self.assertEqual(isGoodArray([29,6,10]), True)
        self.assertEqual(isGoodArray([3,6]), False)
        self.assertEqual(isGoodArray([2,3,4,5,1]), True)
        self.assertEqual(isGoodArray([3,6,5]), True)

if __name__ == "__main__":

    unittest.main()
