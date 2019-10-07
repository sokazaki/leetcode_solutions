# O(N) Solution with Greedy Approach

import unittest


def merge(intervals):

    if len(intervals)==0:
        return []
    intervals = sorted(intervals, key = lambda x: x[0])
    res = [intervals[0]]
    for n in intervals[1:]:
        if n[0] <= res[-1][1]:
            res[-1][1] = max(n[1], res[-1][1])
        else:
            res.append(n)
    return res


class Test(unittest.TestCase):

    def test_merge(self):
        self.assertEqual(merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[1,4],[4,5]]), [[1,5]])
        self.assertEqual(merge([[1,3],[8,10],[2,6],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(merge([[1,3],[3,4],[8,10],[2,6],[18,18]]), [[1,6],[8,10],[18,18]])

if __name__ == "__main__":

    unittest.main()
