# O(N^2) Solution with Sort and Two Pointers

import unittest


def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res


class Test(unittest.TestCase):

    def test_threeSum(self):
        self.assertCountEqual(threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertCountEqual(threeSum([-2,0,0,2,2]), [[-2,0,2]])
        self.assertCountEqual(threeSum([0]), [])
        self.assertCountEqual(threeSum([1,2,3,4,5,6]), [])
        self.assertCountEqual(threeSum([0,0,0,1,0,10,0]), [[0,0,0]])

if __name__ == "__main__":

    unittest.main()
