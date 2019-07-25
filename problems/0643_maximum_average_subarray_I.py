# O(N) Solution with Two Pointers/Sliding Windows

import unittest

def findMaxAverage(nums, k):
    ma = 0
    for i in range(k): ma += nums[i]
    res = ma

    for i in range(len(nums)-k):
        ma = ma - nums[i] + nums[i+k]
        if ma>=res: res = ma
    return res/k


class Test(unittest.TestCase):

    def test_findMaxAverage(self):
        self.assertAlmostEqual(findMaxAverage([1,12,-5,-6,50,3], 4), 12.75, places=7)
        self.assertAlmostEqual(findMaxAverage([1,12,-5,-6,50,3,55,123, -221], 3), 60.3333333, places=7)
        self.assertAlmostEqual(findMaxAverage([1,12,-5,-6,50,3,55,123, -221], 5), 45.0, places=7)
        self.assertAlmostEqual(findMaxAverage([5], 1), 5.0, places=7)

if __name__ == "__main__":

    unittest.main()
