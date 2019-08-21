# O(N) Solution with Two Pointers

import unittest

def findUnsortedSubarray(nums):

    i, j = 0, len(nums)-1
    while i < len(nums)-1 and nums[i] <= nums[i+1]:
        i += 1

    if i == len(nums)-1:
        return 0

    while j > 0 and nums[j] >= nums[j-1]:
        j -= 1


    vmin = min(nums[i:j+1])
    vmax = max(nums[i:j+1])

    while i >= 0 and nums[i] > vmin:
        i -= 1
    while j <= len(nums)-1 and nums[j] < vmax:
        j += 1

    return j-i-1


class Test(unittest.TestCase):

    def test_findUnsortedSubarray(self):
        self.assertEqual(findUnsortedSubarray([2,6,4,8,10,9,15]), 5)
        self.assertEqual(findUnsortedSubarray([1,1,0,1,1,1]), 3)
        self.assertEqual(findUnsortedSubarray([1]), 0)
        self.assertEqual(findUnsortedSubarray([1,2,3,4]), 0)
        self.assertEqual(findUnsortedSubarray([0,0,1,1,1]), 0)
        self.assertEqual(findUnsortedSubarray([0,0,1,1,1,1,0]), 5)


if __name__ == "__main__":

    unittest.main()
