# O(NM) Solution with DFS

import unittest


def maxAreaOfIsland(grid):

    def dfs(i,j):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]:
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        return 0

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
             if grid[i][j]:
                res = max(dfs(i,j), res)

    return res


class Test(unittest.TestCase):

    def test_maxAreaOfIsland(self):
        self.assertEqual(maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]), 4)
        self.assertEqual(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]), 0)
        self.assertEqual(maxAreaOfIsland([[1,0,1,1,1,1,1,0]]), 5)
        self.assertEqual(maxAreaOfIsland([]), 0)

if __name__ == "__main__":

    unittest.main()
