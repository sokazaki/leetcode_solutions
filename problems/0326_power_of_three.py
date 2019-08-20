# O(1) Solution with Simple Approach

import unittest


def isPowerOfThree(n):

    return n > 0 and 3**20 % n == 0


class Test(unittest.TestCase):

    def test_isPowerOfThree(self):
        self.assertEqual(isPowerOfThree(3**20), True)
        self.assertEqual(isPowerOfThree(3**20-1), False)
        self.assertEqual(isPowerOfThree(27), True)
        self.assertEqual(isPowerOfThree(26), False)
        self.assertEqual(isPowerOfThree(0), False)
        self.assertEqual(isPowerOfThree(-3), False)

if __name__ == "__main__":

    unittest.main()
