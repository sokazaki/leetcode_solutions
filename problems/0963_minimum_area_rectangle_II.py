# O(N^3) Solution with Hashmap

import unittest

def minAreaFreeRect(points):
    dic = {(x, y) for x, y in points}
    res = float("inf")
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i+1, len(points)):
            x2, y2 = points[j]
            for k in range(j+1, len(points)):
                x3, y3 = points[k]
                if (x3-x1)*(x2-x1) + (y3-y1)*(y2-y1) == 0 and (x3+(x2-x1), y3+(y2-y1)) in dic:
                    area = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5 * ((x3-x1) ** 2 + (y3-y1) ** 2) ** 0.5
                    res = min(res, area)

    return res if res != float("inf") else 0


class Test(unittest.TestCase):

    def test_minAreaFreeRect(self):
        self.assertAlmostEqual(minAreaFreeRect([[1,1],[1,3],[3,1],[3,3],[2,2]]), 4)
        self.assertAlmostEqual(minAreaFreeRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]), 2)
        self.assertAlmostEqual(minAreaFreeRect([[1,1],[1,3],[3,1],[3,3],[2,2],[4,6],[2,3],[1,2]]), 1)
        self.assertAlmostEqual(minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]), 2)
        self.assertAlmostEqual(minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]]), 0)


if __name__ == "__main__":

    unittest.main()
