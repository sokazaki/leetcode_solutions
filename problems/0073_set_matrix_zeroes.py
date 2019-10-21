# O(NM) Time Complexity / O(1) Space Complexity Solution with Simple Approach

import unittest

def setZeroes(matrix):

    row_zero = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            row_zero = True
    col_zero = False
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            col_zero = True

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(1, len(matrix[0])):
                matrix[i][j] = 0
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(1, len(matrix)):
                matrix[i][j] = 0

    if row_zero:
        for i in range(len(matrix)):
            matrix[i][0] = 0
    if col_zero:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    return matrix


class Test(unittest.TestCase):

    def test_setZeroes(self):
        self.assertEqual(setZeroes([[1,1,1],[1,0,1],[1,1,1]]), [[1,0,1],[0,0,0],[1,0,1]])
        self.assertEqual(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
        self.assertEqual(setZeroes([[1],[-3],[0]]), [[0],[0],[0]])
        self.assertEqual(setZeroes([[1],[-3],[2]]), [[1],[-3],[2]])
        self.assertEqual(setZeroes([[1]]), [[1]])

if __name__ == "__main__":

    unittest.main()
