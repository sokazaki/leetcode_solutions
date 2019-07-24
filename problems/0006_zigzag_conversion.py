# O(N) Solution with simple approach

import unittest

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows-1:
            step = -1
        index += step

    return ''.join(L)

class Test(unittest.TestCase):

    def test_convert(self):
        self.assertEqual(convert("PAYPALISHIRING",3), "PAHNAPLSIIGYIR")
        self.assertEqual(convert("PAYPALISHIRING",4), "PINALSIGYAHRPI")
        self.assertEqual(convert("ABCD",2), "ACBD")
        self.assertEqual(convert("ABCD",1), "ABCD")
        self.assertEqual(convert("AB",2), "AB")
        self.assertEqual(convert("AB",1), "AB")

if __name__ == "__main__":

    unittest.main()
