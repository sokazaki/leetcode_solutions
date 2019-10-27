# O(N^2) Solution with Hashmap

import unittest

def maxPoints(points):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def frac(x, y):
        g = gcd(x, y)
        return x//g, y//g

    res = 0
    for i in range(len(points)):
        dic = {'inf': 1}
        same = 0
        x1, y1 = points[i][0], points[i][1]
        for j in range(i+1, len(points)):
            x2, y2 = points[j][0], points[j][1]
            if x1 == x2 and y1 == y2:
                same += 1
                continue
            if x1-x2 == 0:
                slope = 'inf'
            else:
                slope = frac((x2-x1), (y2-y1))
            if slope not in dic:
                dic[slope] = 1
            dic[slope] += 1

        res = max(res, max(dic.values()) + same)

    return res


class Test(unittest.TestCase):

    def test_maxPoints(self):
        self.assertEqual(maxPoints([[1,1],[2,2],[3,3]]), 3)
        self.assertEqual(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]), 4)
        self.assertEqual(maxPoints([[0,0]]), 1)
        self.assertEqual(maxPoints([[1,1],[1,1],[1,1]]), 3)
        self.assertEqual(maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]), 2)


if __name__ == "__main__":

    unittest.main()
