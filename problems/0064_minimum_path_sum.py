# O(NM) Time Complexity / O(1) Space Complexity Solution with Dynamic Programming

import unittest

def minPathSum(grid):

    if not grid:
        return 0

    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0]
    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i-1]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])

    return grid[-1][-1]


class Test(unittest.TestCase):

    def test_minPathSum(self):
        self.assertEqual(minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7)
        self.assertEqual(minPathSum([[1,3,1],[1,0,1],[4,2,1]]), 4)
        self.assertEqual(minPathSum([[1,3,1,1],[1,5,1,1],[4,2,1,1]]), 8)
        self.assertEqual(minPathSum([[1,3,1]]), 5)

if __name__ == "__main__":

    unittest.main()
