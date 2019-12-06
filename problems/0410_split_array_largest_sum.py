# O(logN) Solution with Binary Search

import unittest


class Solution:
    def is_valid(self, nums, m, mid):
        count, cur_sum  = 1, 0
        for x in nums:
            cur_sum += x
            if cur_sum > mid:
                cur_sum = x
                count += 1
        return count <= m

    def splitArray(self, nums, m):
        low, high, res = max(nums), sum(nums), -1
        while low <= high:
            mid = (low+high)//2
            if self.is_valid(nums, m, mid):
                res, high = mid, mid-1
            else:
                low = mid + 1
        return res


class Test(unittest.TestCase):

    def test_splitArray(self):
        ans = Solution()
        self.assertEqual(ans.splitArray([7,2,5,10,8], 2), 18)
        self.assertEqual(ans.splitArray([7,2,5,10,8,3,7,12,1,5], 3), 24)
        self.assertEqual(ans.splitArray([7,2,5,10,8,3,7,12,1,5], 4), 18)
        self.assertEqual(ans.splitArray([7,2,5,10,8,3,7,12,1,5], 2), 32)
        self.assertEqual(ans.splitArray([7,2,5,1,8], 2), 14)

if __name__ == "__main__":

    unittest.main()
