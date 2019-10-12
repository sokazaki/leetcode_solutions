# O(N^2) Solution with Sort and Two Pointers

import unittest


def threeSumClosest(nums, target):

    nums.sort()
    res = nums[0]+nums[1]+nums[2]

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            if abs(s-target) < abs(res-target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return res

    return res


class Test(unittest.TestCase):

    def test_threeSumClosest(self):
        self.assertEqual(threeSumClosest([-1,2,1,-4], 1), 2)
        self.assertEqual(threeSumClosest([-1,2,1,-4], 2), 2)
        self.assertEqual(threeSumClosest([-1,-1,4,2,1,-4,3,4,2], 1), 1)
        self.assertEqual(threeSumClosest([-1,2,1], 100), 2)
        self.assertEqual(threeSumClosest([-1,2,1,-4], 1), 2)

if __name__ == "__main__":

    unittest.main()
