# O(logN) Solution with Binary Search

import unittest


def search(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low+high) // 2
        if nums[mid]==target:
            return mid

        if nums[low]<=nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high = mid-1
            else:
                low = mid+1
        elif nums[low]>nums[mid]:
            if nums[mid]<=target<=nums[high]:
                low = mid+1
            else:
                high = mid-1

    return -1


class Test(unittest.TestCase):

    def test_search(self):
        self.assertEqual(search([4,5,6,7,0,1,2], 0), 4)
        self.assertEqual(search([4,5,6,7,0,1,2], 3), -1)
        self.assertEqual(search([4,5,6,7,8,9,10,11,0,1,2], 11), 7)
        self.assertEqual(search([5,1,3], 2), -1)
        self.assertEqual(search([], 0), -1)

if __name__ == "__main__":

    unittest.main()
