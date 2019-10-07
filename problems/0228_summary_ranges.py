# O(N) Solution with Simple Approach

import unittest


class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        res, i, start = [], 0, 0
        while i < len(nums)-1:
            if nums[i]+1 != nums[i+1]:
                res.append(self.helper(nums[start], nums[i]))
                start = i+1
            i += 1
        res.append(self.helper(nums[start], nums[i]))
        return res

    def helper(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)


class Test(unittest.TestCase):

    def test_summaryRanges(self):
        ans = Solution()
        self.assertEqual(ans.summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])
        self.assertEqual(ans.summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])
        self.assertEqual(ans.summaryRanges([]), [])
        self.assertEqual(ans.summaryRanges([-1]), ["-1"])
        self.assertEqual(ans.summaryRanges([0,1,2,3,4,5,6,8,9]), ["0->6","8->9"])

if __name__ == "__main__":

    unittest.main()
