# O(N^3) Solution with Sort and Two Pointers

import unittest


def fourSum(nums, target):
    res = []
    nums.sort()
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        if nums[i] * 4 > target:
            break

        for j in range(i+1, len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            if nums[j] * 3 > target-nums[i]:
                break

            l, r = j+1, len(nums)-1

            while l < r:

                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1

    return res


class Test(unittest.TestCase):

    def test_fourSum(self):
        self.assertCountEqual(fourSum([1,0,-1,0,-2,2],0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        self.assertCountEqual(fourSum([11,0,-1,0,-2,2],2), [])
        self.assertCountEqual(fourSum([11,0,-1,0,-2,2,1,-1,-2,-1,3,4,-5], 2), [[-5,-2,-2,11],[-5,0,3,4],[-5,1,2,4],[-2,-2,2,4],[-2,-1,1,4],[-2,-1,2,3],[-2,0,0,4],[-2,0,1,3],[-1,-1,0,4],[-1,-1,1,3],[-1,0,0,3],[-1,0,1,2]])
        self.assertCountEqual(fourSum([0,0,0,0],0), [[0,0,0,0]])
        self.assertCountEqual(fourSum([0,0,0,0,1,1,-1,0,1,-1],0), [[-1,-1,1,1],[-1,0,0,1],[0,0,0,0]])

if __name__ == "__main__":

    unittest.main()
