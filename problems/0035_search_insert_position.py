# O(logN) Solution with Binary Search

import unittest
import bisect

def searchInsert(nums, target):
    return bisect.bisect_left(nums, target)


class Test(unittest.TestCase):

    def test_searchInsert(self):
        self.assertEqual(searchInsert([1,3,5,6], 5), 2)
        self.assertEqual(searchInsert([1,3,5,6], 2), 1)
        self.assertEqual(searchInsert([1,3,5,6], 7), 4)
        self.assertEqual(searchInsert([1,3,5,6], 0), 0)
        self.assertEqual(searchInsert([1], 0), 0)

if __name__ == "__main__":

    unittest.main()
