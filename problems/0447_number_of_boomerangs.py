# O(N^2) Solution with Hashmap

import unittest
from collections import defaultdict

def numberOfBoomerangs(points):
    res = 0
    for x1, y1 in points:
        dic = defaultdict(int)
        for x2, y2 in points:
            d1 = x2-x1
            d2 = y2-y1
            dic[d1**2+d2**2] += 1
        for k in dic:
            res += dic[k] * (dic[k]-1)
    return res


class Test(unittest.TestCase):

    def test_numberOfBoomerangs(self):
        self.assertEqual(numberOfBoomerangs([[0,0],[1,0],[2,0]]), 2)
        self.assertEqual(numberOfBoomerangs([[0,0],[1,0],[2,0],[3,0]]), 4)
        self.assertEqual(numberOfBoomerangs([[0,0],[1,0],[2,0],[3,0],[4,0]]), 8)
        self.assertEqual(numberOfBoomerangs([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0]]), 12)
        self.assertEqual(numberOfBoomerangs([[0,0],[1,0]]), 0)


if __name__ == "__main__":

    unittest.main()
