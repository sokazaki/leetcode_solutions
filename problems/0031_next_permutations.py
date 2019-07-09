# O(N) Worst Case Time Complexity / O(1) Amortized Time Complexity

import unittest

def nextPermutation(nums):
    i = j = len(nums)-1
    while i>0 and nums[i-1]>=nums[i]:
        i -= 1
    if i==0:   # nums are in descending order
        nums.reverse()
        return nums
    k = i-1    # find the last "ascending" position
    while nums[j]<=nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]
    l, r = k+1, len(nums)-1  # reverse the second part
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1

    return nums

class Test(unittest.TestCase):

    def test_nextPermutation(self):
        self.assertListEqual(nextPermutation([1,2,3]), [1,3,2])
        self.assertListEqual(nextPermutation([3,2,1]), [1,2,3])
        self.assertListEqual(nextPermutation([1,1,5]), [1,5,1])

if __name__ == "__main__":

    unittest.main()
