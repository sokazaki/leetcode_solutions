# O(N) Solution with Greedy Approach

import unittest

def jump(nums):
    if len(nums) <= 1:
        return 0
    left, right = 0, nums[0]
    res = 1
    while right < len(nums)-1:
        res += 1
        curmax = max(idx + nums[idx] for idx in range(left, right+1))
        left, right = right, curmax
    return res

class Test(unittest.TestCase):

    def test_canJump(self):
        self.assertEqual(jump([2,3,1,1,4]), 2)
        self.assertEqual(jump([3,2,1,1,4]), 2)
        self.assertEqual(jump([0]), 0)
        self.assertEqual(jump([5,4]), 1)
        self.assertEqual(jump([4,0,0,0,4]), 1)


if __name__ == "__main__":

    unittest.main()
