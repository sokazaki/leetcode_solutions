# O(N) Solution with Simple Approach

import unittest
from collections import Counter

def intersect(nums1, nums2):
    return list((Counter(nums1) & Counter(nums2)).elements())


class Test(unittest.TestCase):

    def test_intersect(self):
        self.assertCountEqual(intersect([1,2,2,1], [2,2]), [2,2])
        self.assertCountEqual(intersect([4,9,5], [9,4,9,8,4]), [9,4])
        self.assertCountEqual(intersect([1,2,3,4,5], []), [])
        self.assertCountEqual(intersect([1,2,2,1], [2,2,1,1]), [1,1,2,2])
        self.assertCountEqual(intersect([], []), [])

if __name__ == "__main__":

    unittest.main()
