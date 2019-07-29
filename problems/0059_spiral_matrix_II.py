# O(NM) Solution with Simple Approach

import unittest

def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        matrix[i][j] = k + 1
        if matrix[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return matrix

class Test(unittest.TestCase):

    def test_generateMatrix(self):
        self.assertListEqual(generateMatrix(1), [[1]])
        self.assertListEqual(generateMatrix(2), [[1,2],[4,3]])
        self.assertListEqual(generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])
        self.assertListEqual(generateMatrix(4), [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]])
        self.assertListEqual(generateMatrix(5), [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]])

if __name__ == "__main__":

    unittest.main()
