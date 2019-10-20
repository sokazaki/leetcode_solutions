# O(logN) Solution with Binary Search

import unittest


def findMin(nums):

    low, high = 0, len(nums)-1
    while low < high:
        mid = low + (high-low)//2
        if nums[mid] > nums[high]:
            low = mid+1
        else:
            high = mid
    return nums[low]


class Test(unittest.TestCase):

    def test_rfindMin(self):
        self.assertEqual(findMin([3,4,5,1,2]), 1)
        self.assertEqual(findMin([4,5,6,7,0,1,2]), 0)
        self.assertEqual(findMin([4,5,6,7,10,11,12]), 4)
        self.assertEqual(findMin([4,5]), 4)
        self.assertEqual(findMin([4]), 4)

if __name__ == "__main__":

    unittest.main()
