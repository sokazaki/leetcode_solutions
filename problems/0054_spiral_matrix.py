# O(NM) Solution with Simple Approach

import unittest

def spiralOrder(matrix):
    res = []

    i, j, di, dj = 0, 0, 0, 1
    if not matrix: return []
    for k in range(len(matrix)*len(matrix[0])):
        res.append(matrix[i][j])
        matrix[i][j] = ""
        if matrix[(i+di)%len(matrix)][(j+dj)%len(matrix[0])]=="":
            di, dj = dj, -di
        i += di
        j += dj
    return res

class Test(unittest.TestCase):

    def test_spiralOrder(self):
        self.assertListEqual(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,3,6,9,8,7,4,5])
        self.assertListEqual(spiralOrder([[3],[2]]), [3,2])
        self.assertListEqual(spiralOrder([]), [])
        self.assertListEqual(spiralOrder([[1]]), [1])
        self.assertListEqual(spiralOrder([[3,2]]), [3,2])

if __name__ == "__main__":

    unittest.main()
