# Simple Solution with Bit Manipulation

import unittest


def isPowerOfTwo(n):

    return n > 0 and not (n & n-1)


class Test(unittest.TestCase):

    def test_isPowerOfTwo(self):
        self.assertEqual(isPowerOfTwo(2**32), True)
        self.assertEqual(isPowerOfTwo(2**32-1), False)
        self.assertEqual(isPowerOfTwo(16), True)
        self.assertEqual(isPowerOfTwo(15), False)
        self.assertEqual(isPowerOfTwo(0), False)
        self.assertEqual(isPowerOfTwo(-2), False)

if __name__ == "__main__":

    unittest.main()
