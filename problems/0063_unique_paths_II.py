# In-Place Solution with Dynamic Programming

import unittest

def uniquePathsWithObstacles(obstacleGrid):

    if not obstacleGrid or obstacleGrid[0][0]:
        return 0

    obstacleGrid[0][0] = 1
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    for i in range(1,m):
        obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1-obstacleGrid[i][0])

    for j in range(1,n):
        obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1-obstacleGrid[0][j])

    for i in range(1,m):
        for j in range(1,n):
            obstacleGrid[i][j] = (1-obstacleGrid[i][j]) * (obstacleGrid[i-1][j]+obstacleGrid[i][j-1])

    return obstacleGrid[-1][-1]


class Test(unittest.TestCase):

    def test_uniquePathsWithObstacles(self):
        self.assertEqual(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]), 2)
        self.assertEqual(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,1]]), 0)
        self.assertEqual(uniquePathsWithObstacles([[1,0,0],[0,1,0],[0,0,0]]), 0)
        self.assertEqual(uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0]]), 6)
        self.assertEqual(uniquePathsWithObstacles([[0,0,0],[0,0,0],[0,0,0],[0,0,0]]), 10)
        self.assertEqual(uniquePathsWithObstacles([]), 0)


if __name__ == "__main__":

    unittest.main()
