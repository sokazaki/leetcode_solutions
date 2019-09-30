# O(N+M) Solution with Simple Approach

import unittest

def searchMatrix(matrix, target):

    if not matrix:
        return False

    row, col = 0, len(matrix[0])-1
    while row<=len(matrix)-1 and 0<=col:
        cur = matrix[row][col]
        if cur == target:
            return True
        elif cur > target:
            col -= 1
        else:
            row += 1

    return False


class Test(unittest.TestCase):

    def test_searchMatrix(self):
        self.assertEqual(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5), True)
        self.assertEqual(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20), False)
        self.assertEqual(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],31), False)
        self.assertEqual(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],0), False)
        self.assertEqual(searchMatrix([[1]],1), True)
        self.assertEqual(searchMatrix([[]],1), False)

if __name__ == "__main__":

    unittest.main()
