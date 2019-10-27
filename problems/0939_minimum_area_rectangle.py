# O(N^2) Solution with Hashmap

import unittest

def minAreaRect(points):
    res = float("inf")
    dic = set()
    for x, y in points:
        dic.add((x,y))

    for x1, y1 in points:
        for x2, y2 in points:
            if x1 > x2 and y1 > y2:
                if (x1, y2) in dic and (x2, y1) in dic:
                    area = (x1-x2) * (y1-y2)
                    res = min(area, res)

    return 0 if res == float("inf") else res


class Test(unittest.TestCase):

    def test_minAreaRect(self):
        self.assertEqual(minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]), 4)
        self.assertEqual(minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]), 2)
        self.assertEqual(minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2],[4,6],[2,3],[1,2]]), 1)
        self.assertEqual(minAreaRect([[1,2],[2,1],[1,0],[0,1]]), 0)
        self.assertEqual(minAreaRect([[0,3],[1,2],[3,1],[1,3],[2,1]]), 0)


if __name__ == "__main__":

    unittest.main()
