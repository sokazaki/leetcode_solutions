# O(1) Solution with Bit Manipulation

import unittest

def getSum(a, b):
    carry = 0
    mask = 0xffffffff
    while b & mask != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return a&mask if b > mask else a


class Test(unittest.TestCase):

    def test_getSum(self):
        self.assertEqual(getSum(1, 2), 3)
        self.assertEqual(getSum(1, -1), 0)
        self.assertEqual(getSum(3, -1), 2)
        self.assertEqual(getSum(-1, 3), 2)
        self.assertEqual(getSum(0, -1), -1)
        self.assertEqual(getSum(99, 45), 144)

if __name__ == "__main__":

    unittest.main()
