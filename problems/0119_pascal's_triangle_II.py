# O(N^2) Solution with Simple Approach

import unittest


def getRow(rowIndex):

    res = [0] * (rowIndex+1)
    res[0] = 1
    for i in range(1, rowIndex+1):
        for j in range(i, 0, -1):
            res[j] += res[j-1]

    return res


class Test(unittest.TestCase):

    def test_getRow(self):
        self.assertEqual(getRow(1), [1,1])
        self.assertEqual(getRow(2), [1,2,1])
        self.assertEqual(getRow(3), [1,3,3,1])
        self.assertEqual(getRow(7), [1,7,21,35,35,21,7,1])
        self.assertEqual(getRow(10), [1,10,45,120,210,252,210,120,45,10,1])

if __name__ == "__main__":

    unittest.main()
