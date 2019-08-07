# O(N) Solution with DFS

import unittest

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return 0
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


class Test(unittest.TestCase):

    def test_numIslands(self):
        ans = Solution()
        self.assertEqual(ans.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]), 1)
        self.assertEqual(ans.numIslands([["1","0","1","1","0"]]), 2)
        self.assertEqual(ans.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","1"],["0","0","1","0","0"]]), 3)
        self.assertEqual(ans.numIslands([["1","0","0","1"],["1","1","0","1"],["1","1","0","0"],["0","0","0","0"]]), 2)


if __name__ == "__main__":

    unittest.main()
