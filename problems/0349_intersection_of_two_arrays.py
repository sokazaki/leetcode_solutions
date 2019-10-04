# O(N) Solution with Simple Approach

import unittest

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


class Test(unittest.TestCase):

    def test_intersection(self):
        self.assertCountEqual(intersection([1,2,2,1], [2,2]), [2])
        self.assertCountEqual(intersection([4,9,5], [9,4,9,8,4]), [9,4])
        self.assertCountEqual(intersection([1,2,3,4,5], []), [])
        self.assertCountEqual(intersection([1,2,2,1], [2,2,1,1]), [1,2])
        self.assertCountEqual(intersection([], []), [])

if __name__ == "__main__":

    unittest.main()
