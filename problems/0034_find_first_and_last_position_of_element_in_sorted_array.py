# O(logN) Solution with Binary Search

import unittest
import bisect

def searchRange(nums, target):
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)
    if left>=len(nums) or nums[left] != target and nums[right-1] != target:
        return [-1, -1]
    return [left, right-1]


class Test(unittest.TestCase):

    def test_searchRange(self):
        self.assertEqual(searchRange([5,7,7,8,8,10], 8), [3, 4])
        self.assertEqual(searchRange([5,7,7,8,8,10], 6), [-1, -1])
        self.assertEqual(searchRange([5,7,7,8,8,10], 12), [-1, -1])
        self.assertEqual(searchRange([5], 5), [0, 0])
        self.assertEqual(searchRange([5], 2), [-1, -1])

if __name__ == "__main__":

    unittest.main()
