# O(NM) Time Complexity / O(1) Space Complexity Solution with Simple Approach

import unittest

def flipAndInvertImage(A):

    if not A:
        return []

    return [[1-i for i in row[::-1]] for row in A]


class Test(unittest.TestCase):

    def test_flipAndInvertImage(self):
        self.assertEqual(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]), [[1,0,0],[0,1,0],[1,1,1]])
        self.assertEqual(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]), [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]])
        self.assertEqual(flipAndInvertImage([]), [])
        self.assertEqual(flipAndInvertImage([[0,0,0,0,1]]), [[0,1,1,1,1]])


if __name__ == "__main__":

    unittest.main()
