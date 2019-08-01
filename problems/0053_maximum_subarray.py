# O(N) Solution with Kadane's Algorithm / O(NlogN) Solution with Divide and Conquer

import unittest

# Kadane's Algorithm
def maxSubArray_kadane(nums):
    if not nums:
        return 0

    cur = res = nums[0]
    for num in nums[1:]:
        cur = max(num, cur + num)
        res = max(res, cur)

    return res

# Divide and Conquer Approach
class Solution:
    def helper(self, nums, l, r):

        if l > r:
            return -float("inf")

        m = int((l+r)/2)

        left_max = tmp = 0
        for i in range(m-1, l-1, -1):
            tmp += nums[i]
            left_max = max(left_max, tmp)

        right_max = tmp = 0
        for i in range(m+1, r+1):
            tmp += nums[i]
            right_max = max(right_max, tmp)

        left_ans = self.helper(nums, l, m-1)
        right_ans = self.helper(nums, m+1, r)

        return max(left_max+nums[m]+right_max, max(left_ans, right_ans))

    def maxSubArray_divide_and_conquer(self, nums):

        return self.helper(nums, 0, len(nums)-1)

class Test(unittest.TestCase):

    def test_maxSubArray_kadane(self):
        self.assertEqual(maxSubArray_kadane([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maxSubArray_kadane([-2,1,3,4,-11,2,11,-5,7]), 15)
        self.assertEqual(maxSubArray_kadane([6,-1,3,-4,11,2,-11,5,9,8,-10,22,15]), 55)
        self.assertEqual(maxSubArray_kadane([1,2,3,4,5,6]), 21)
        self.assertEqual(maxSubArray_kadane([-1,-2,-3,-4,-5,-6]), -1)
        self.assertEqual(maxSubArray_kadane([1]), 1)

    def test_maxSubArray_divide_and_conquer(self):
        ans = Solution()
        self.assertEqual(ans.maxSubArray_divide_and_conquer([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(ans.maxSubArray_divide_and_conquer([-2,1,3,4,-11,2,11,-5,7]), 15)
        self.assertEqual(ans.maxSubArray_divide_and_conquer([6,-1,3,-4,11,2,-11,5,9,8,-10,22,15]), 55)
        self.assertEqual(ans.maxSubArray_divide_and_conquer([1,2,3,4,5,6]), 21)
        self.assertEqual(ans.maxSubArray_divide_and_conquer([-1,-2,-3,-4,-5,-6]), -1)
        self.assertEqual(ans.maxSubArray_divide_and_conquer([1]), 1)

if __name__ == "__main__":

    unittest.main()
