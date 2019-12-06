# Solution with Dynamic Programming and BFS

import unittest
from functools import lru_cache


def minKnightMoves(x, y):

    @lru_cache(maxsize=None)
    def dp(x,y):
        if x + y == 0:
            return 0
        elif x + y == 2:
            return 2
        return min(dp(abs(x-1), abs(y-2)), dp(abs(x-2), abs(y-1))) + 1

    return dp(abs(x), abs(y))


def minKnightMoves2(x, y):
    if (x, y) == (0, 0):
        return 0
    def bfs(i, j, x, y):
        queue = [(i, j, 0)]
        seen = {(i, j)}
        for i, j, d in queue:
            for di, dj in [(1,2), (2,1), (1,-2), (2,-1),
                           (-1,2), (-2,1), (-1,-2), (-2,-1)]:
                r, c = i+di, j+dj
                if (r,c) not in seen and r>=-2 and c>=-2:
                    if (r,c) == (x,y):
                        return d+1
                    seen.add((r, c))
                    queue.append((r, c, d+1))

    return bfs(0, 0, abs(x), abs(y))


class Test(unittest.TestCase):

    def test_minKnightMoves(self):
        self.assertEqual(minKnightMoves(2, 1), 1)
        self.assertEqual(minKnightMoves(5, 5), 4)
        self.assertEqual(minKnightMoves(1, 1), 2)
        self.assertEqual(minKnightMoves(0, 0), 0)
        self.assertEqual(minKnightMoves(114, -179), 99)
        self.assertEqual(minKnightMoves(-150, 150), 100)


    def test_minKnightMoves2(self):
        self.assertEqual(minKnightMoves2(2, 1), 1)
        self.assertEqual(minKnightMoves2(5, 5), 4)
        self.assertEqual(minKnightMoves2(1, 1), 2)
        self.assertEqual(minKnightMoves2(0, 0), 0)
        self.assertEqual(minKnightMoves2(114, -179), 99)
        self.assertEqual(minKnightMoves2(-150, 150), 100)

if __name__ == "__main__":

    unittest.main()
