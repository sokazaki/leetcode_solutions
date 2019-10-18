# O(NlogN) Solution with Dynamic Programming + Binary Search

import unittest
import bisect

def lengthOfLIS(nums):

    if not nums:
        return 0
    dp = [nums[0]]
    for i in range(len(nums)):
        if nums[i] > dp[-1]:
            dp.append(nums[i])
        else:
            dp[bisect.bisect_left(dp, nums[i])] = nums[i]

    return len(dp)


class Test(unittest.TestCase):

    def test_lengthOfLIS(self):
        self.assertEqual(lengthOfLIS([10,9,2,5,3,7,101,18]), 4)
        self.assertEqual(lengthOfLIS([]), 0)
        self.assertEqual(lengthOfLIS([10,9,2,5,6,7,101,18]), 5)
        self.assertEqual(lengthOfLIS([10,9,2,5,-3,7,101,18]), 4)

if __name__ == "__main__":

    unittest.main()
