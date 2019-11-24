# O(N) Solution with Greedy

import unittest

def insert(intervals, newInterval):
    if len(intervals)==0:
        return [newInterval]

    intervals.append(newInterval)
    intervals = sorted(intervals, key = lambda x: x[0])
    res = [intervals[0]]

    for n in intervals[1:]:
        if n[0] <= res[-1][1]:
            res[-1][1] = max(n[1], res[-1][1])
        else:
            res.append(n)

    return res


class Test(unittest.TestCase):

    def test_insert(self):
        self.assertEqual(insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
        self.assertEqual(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
        self.assertEqual(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
        self.assertEqual(insert([], [4,8]), [[4,8]])
        self.assertEqual(insert([[1,2]], [1,2]), [[1,2]])

if __name__ == "__main__":

    unittest.main()
