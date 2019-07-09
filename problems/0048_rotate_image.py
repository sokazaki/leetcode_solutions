# Simple Solution with zip function and In-Place Solution with tmp variable

import unittest

def rotate(A):
    A[::] = zip(*A[::-1])

    return A

# explicit in-place
def rotate2(A):
    n = len(A)
    # transpose
    for i in range(n):
        for j in range(i+1, n):
            tmp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = tmp
    # flip horizontally
    for i in range(n):
        for j in range(int(n/2)):
            tmp = A[i][j]
            A[i][j] = A[i][n-1-j]
            A[i][n-1-j] = tmp

    return A

class Test(unittest.TestCase):

    def test_rotate(self):
        self.assertListEqual(rotate([[1,2,3],[4,5,6],[7,8,9]]), [(7,4,1),(8,5,2),(9,6,3)])
        self.assertListEqual(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]), [(15,13,2,5),(14,3,4,1),(12,6,8,9),(16,7,10,11)])
        self.assertListEqual(rotate([[1,2],[2,1]]), [(2,1),(1,2)])
        self.assertListEqual(rotate([[1,]]), [(1,)])

    def test_rotate2(self):
        self.assertListEqual(rotate2([[1,2,3],[4,5,6],[7,8,9]]), [[7,4,1],[8,5,2],[9,6,3]])
        self.assertListEqual(rotate2([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]), [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
        self.assertListEqual(rotate2([[1,2],[2,1]]), [[2,1],[1,2]])
        self.assertListEqual(rotate2([[1,]]), [[1,]])

if __name__ == "__main__":

    unittest.main()
