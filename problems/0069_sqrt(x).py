# O(logN) Solution with Binary Search

import unittest

def mySqrt(x):
    low, high = 0, x
    while low <= high:
        mid = low + (high-low)//2
        if mid * mid <= x < (mid+1)*(mid+1):
            return mid
        elif x < mid * mid:
            high = mid
        else:
            low = mid + 1

class Test(unittest.TestCase):

    def test_mySqrt(self):
        self.assertEqual(mySqrt(37), 6)
        self.assertEqual(mySqrt(36), 6)
        self.assertEqual(mySqrt(35), 5)
        self.assertEqual(mySqrt(4), 2)
        self.assertEqual(mySqrt(8), 2)
        self.assertEqual(mySqrt(1), 1)


if __name__ == "__main__":

    unittest.main()
