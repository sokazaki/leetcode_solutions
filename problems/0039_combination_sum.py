# Solution with Backtracking

import unittest


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, idx, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(idx, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)


class Test(unittest.TestCase):

    def test_combinationSum(self):
        ans = Solution()
        self.assertCountEqual(ans.combinationSum([2,3,6,7], 7), [[7],[2,2,3]])
        self.assertCountEqual(ans.combinationSum([], 0), [[]])
        self.assertCountEqual(ans.combinationSum([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]])
        self.assertCountEqual(ans.combinationSum([2,3,6,7], 9), [[2,2,2,3],[2,7],[3,3,3],[3,6]])
        self.assertCountEqual(ans.combinationSum([2,3,6,7], 1), [])
        self.assertCountEqual(ans.combinationSum([2,3,6,7], 11), [[2,2,2,2,3],[2,2,7],[2,3,3,3],[2,3,6]])

if __name__ == "__main__":

    unittest.main()
