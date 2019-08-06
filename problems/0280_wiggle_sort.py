# O(N) Solution with Greedy Sort Approach

import unittest

def wiggleSort(nums):

    for i in range(1, len(nums)):
        if i%2==0 and nums[i]>nums[i-1] or i%2==1 and nums[i]<=nums[i-1]:
            nums[i], nums[i-1] = nums[i-1], nums[i]

    return nums


class Test(unittest.TestCase):

    def test_wiggleSort(self):
        self.assertListEqual(wiggleSort([3,5,2,1,6,4]), [3,5,1,6,2,4])
        self.assertListEqual(wiggleSort([3,-5,2,-1,66,-4]), [-5,3,-1,66,-4,2])
        self.assertListEqual(wiggleSort([1,2,2,1,2,1,1,1,1,2,2,2]), [1,2,1,2,1,2,1,1,1,2,2,2])
        self.assertListEqual(wiggleSort([1,2,0,1,2,-1,0,1,-1,2,2,-2]), [1,2,0,2,-1,1,0,1,-1,2,-2,2])


if __name__ == "__main__":

    unittest.main()
