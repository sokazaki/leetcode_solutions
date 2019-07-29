# O(N*M) Solution with Hash Map

import unittest

def islandPerimeter(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                res += 4
                if i and grid[i-1][j]:
                    res -= 2
                if j and grid[i][j-1]:
                    res -= 2
    return res


class Test(unittest.TestCase):

    def test_islandPerimeter(self):
        self.assertEqual(islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]), 16)
        self.assertEqual(islandPerimeter([[0,1,0,0],[1,1,1,1],[0,1,1,0],[1,1,0,0]]), 18)
        self.assertEqual(islandPerimeter([[0,1,1,0],[0,1,1,1],[0,1,1,0],[1,1,1,1]]), 18)
        self.assertEqual(islandPerimeter([[1,0]]), 4)
        self.assertEqual(islandPerimeter([[1],[0]]), 4)

if __name__ == "__main__":

    unittest.main()
