# Simple Solution with Bit Manipulation

import unittest


def encode(num):
    if num==0:
        return ""
    i=1
    cum = 0
    digit = 0
    while cum<num:
        i *=2
        cum += i
        digit += 1

    return (digit-len(bin(num-cum//2)[2:])) * "0" + bin(num-cum//2)[2:]


class Test(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(encode(0), "")
        self.assertEqual(encode(1), "0")
        self.assertEqual(encode(3), "00")
        self.assertEqual(encode(6), "11")
        self.assertEqual(encode(19), "0100")
        self.assertEqual(encode(23), "1000")
        self.assertEqual(encode(107), "101100")

if __name__ == "__main__":

    unittest.main()
