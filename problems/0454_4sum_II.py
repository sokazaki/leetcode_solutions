# O(N^2) Solution with Hash Table

import unittest


def fourSumCount(A, B, C, D):
    dic = {}
    for a in A:
        for b in B:
            if a+b in dic:
                dic[a+b] += 1
            else:
                dic[a+b] = 1
    res = 0
    for c in C:
        for d in D:
            if -c-d in dic:
                res += dic[-c-d]
    return res


class Test(unittest.TestCase):

    def test_fourSumCount(self):
        self.assertEqual(fourSumCount([1,2], [-2,-1], [-1,2], [0,2]), 2)
        self.assertEqual(fourSumCount([1,2,3], [-2,-1,0], [-1,2,5], [0,2,-3]), 7)
        self.assertEqual(fourSumCount([1,2,3,4,5], [-2,-1,0,-1,-3], [-1,2,5,0,3], [0,2,-3,1,2]), 39)
        self.assertEqual(fourSumCount([], [], [], []), 0)
        self.assertEqual(fourSumCount([1], [-1], [2], [0]), 0)

if __name__ == "__main__":

    unittest.main()
