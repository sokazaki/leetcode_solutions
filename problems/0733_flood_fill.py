# O(NM) Solution with DFS

import unittest

def floodFill(image, sr, sc, newColor):

    def dfs(i, j):
        image[i][j] = newColor
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == old:
                dfs(x, y)

    old = image[sr][sc]
    if old != newColor:
        dfs(sr, sc)

    return image


class Test(unittest.TestCase):

    def test_floodFill(self):
        self.assertEqual(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]])
        self.assertEqual(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 1), [[1,1,1],[1,1,0],[1,0,1]])
        self.assertEqual(floodFill([[1,1,1],[1,1,0],[1,0,1]], 2, 2, 2), [[1,1,1],[1,1,0],[1,0,2]])
        self.assertEqual(floodFill([[1,1,1,0,1]],0,1,2), [[2,2,2,0,1]])
        self.assertEqual(floodFill([[1,11,111,0,1]], 0,4,2), [[1,11,111,0,2]])


if __name__ == "__main__":

    unittest.main()
