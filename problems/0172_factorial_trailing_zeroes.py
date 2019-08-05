# O(log_5 N) Solution with Simple Approach

import unittest

def trailingZeroes(n):
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res


class Test(unittest.TestCase):

    def test_trailingZeroes(self):
        self.assertEqual(trailingZeroes(3), 0)
        self.assertEqual(trailingZeroes(5), 1)
        self.assertEqual(trailingZeroes(10), 2)
        self.assertEqual(trailingZeroes(100), 24)
        self.assertEqual(trailingZeroes(1000), 249)
        self.assertEqual(trailingZeroes(0), 0)
        self.assertEqual(trailingZeroes(1), 0)

if __name__ == "__main__":

    unittest.main()
