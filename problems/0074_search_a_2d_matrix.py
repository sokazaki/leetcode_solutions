# O(logNM) Solution with Binary Search

import unittest
import bisect

def searchMatrix(matrix, target):

    if not matrix:
        return False

    i = bisect.bisect_left(matrix, [target])
    if i < len(matrix) and matrix[i][0] == target:
        return True

    j = bisect.bisect_left(matrix[i-1], target)
    return j < len(matrix[0]) and matrix[i-1][j] == target


class Test(unittest.TestCase):

    def test_searchMatrix(self):
        self.assertEqual(searchMatrix([[1],[3]],1), True)
        self.assertEqual(searchMatrix([],0), False)
        self.assertEqual(searchMatrix([[]],1), False)
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3), True)
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],13), False)

if __name__ == "__main__":

    unittest.main()
