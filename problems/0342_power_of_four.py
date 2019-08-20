# O(1) Solution with Simple Approach

import unittest


def isPowerOfFour(num):

    return num > 0 and num & (num-1) == 0 and len(bin(num)[2:])%2 == 1


class Test(unittest.TestCase):

    def test_isPowerOfFour(self):
        self.assertEqual(isPowerOfFour(4**10), True)
        self.assertEqual(isPowerOfFour(4**10-1), False)
        self.assertEqual(isPowerOfFour(64), True)
        self.assertEqual(isPowerOfFour(63), False)
        self.assertEqual(isPowerOfFour(1), True)
        self.assertEqual(isPowerOfFour(0), False)
        self.assertEqual(isPowerOfFour(-4), False)

if __name__ == "__main__":

    unittest.main()
