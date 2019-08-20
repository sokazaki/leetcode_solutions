# O(N) Solution with Built-In Method

import unittest


def reverseBits(n):

    return int(bin(n)[2:].rjust(32, '0')[::-1], 2)


class Test(unittest.TestCase):

    def test_reverseBits(self):
        self.assertEqual(reverseBits(2**32), 1)
        self.assertEqual(reverseBits(2**32-1), 4294967295)
        self.assertEqual(reverseBits(16), 134217728)
        self.assertEqual(reverseBits(15), 4026531840)
        self.assertEqual(reverseBits(0), 0)

if __name__ == "__main__":

    unittest.main()
