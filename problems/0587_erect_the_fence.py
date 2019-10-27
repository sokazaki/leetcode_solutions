# O(NlogN) Solution with Sort + Greedy (Andrew's Convex Hull Algorithm)

import unittest

def outerTrees(points):

    points = sorted(points, key=lambda p: (p[0], p[1]))

    if len(points) <= 1:
        return points

    def check_direction(p0, p1, p2):
        return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p1[1] - p0[1]) * (p2[0] - p0[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and check_direction(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and check_direction(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    def helper(seq):
        seen = []
        return [x for x in seq if x not in seen and not seen.append(x)]

    return helper(lower[:-1] + upper[:-1])


class Test(unittest.TestCase):

    def test_outerTrees(self):
        self.assertEqual(outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]), [[1,1],[2,0],[4,2],[3,3],[2,4]])
        self.assertEqual(outerTrees([[1,2],[2,2],[4,2]]), [[1,2],[2,2],[4,2]])
        self.assertEqual(outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2],[5,3],[2,3]]), [[1,1],[2,0],[4,2],[5,3],[2,4]])
        self.assertEqual(outerTrees([[1,1],[2,2]]), [[1,1],[2,2]])
        self.assertEqual(outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2],[0,0],[0,4],[4,4],[4,0]]), [[0,0],[2,0],[4,0],[4,2],[4,4],[2,4],[0,4]])


if __name__ == "__main__":

    unittest.main()
