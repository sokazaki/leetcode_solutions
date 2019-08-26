# O(NM) Time Complexity / O(NM) Space Complexity Solution with Dynamic Programming

import unittest

def maximalSquare(matrix):

    if not matrix:
        return 0

    res = 0
    for i in range(len(matrix)):
        matrix[i][0] = int(matrix[i][0])
        if matrix[i][0] == 1:
            res = 1

    for i in range(len(matrix[0])):
        matrix[0][i] = int(matrix[0][i])
        if matrix[0][i] == 1:
            res = 1

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == "1":
                matrix[i][j] = min([matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]])+1
                res = max(res, matrix[i][j])
            else:
                matrix[i][j] = 0

    return res**2


class Test(unittest.TestCase):

    def test_maximalSquare(self):
        self.assertEqual(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), 4)
        self.assertEqual(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","1"]]), 9)
        self.assertEqual(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","0","1"],["1","0","0","1","0"]]), 1)
        self.assertEqual(maximalSquare([["1","0","1","0"],["1","0","1","1"],["1","1","1","1"],["1","0","0","1"]]), 4)

if __name__ == "__main__":

    unittest.main()
