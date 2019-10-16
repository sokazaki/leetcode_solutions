# O(N) Solution with Bit Manipulation

import unittest


def validUtf8(data):

    count = 0
    for c in data:
        if (count == 0):
            if ((c >> 5) == 0b110): count = 1
            elif ((c >> 4) == 0b1110): count = 2
            elif ((c >> 3) == 0b11110): count = 3
            elif ((c >> 7)): return False
        else:
            if ((c >> 6) != 0b10): return False
            count -= 1

    return count == 0


class Test(unittest.TestCase):

    def test_validUtf8(self):
        self.assertEqual(validUtf8([197,130,1]), True)
        self.assertEqual(validUtf8([235,140,4]), False)
        self.assertEqual(validUtf8([197,1,130]), False)
        self.assertEqual(validUtf8([235,140,130,4]), True)
        self.assertEqual(validUtf8([197]), False)

if __name__ == "__main__":

    unittest.main()
