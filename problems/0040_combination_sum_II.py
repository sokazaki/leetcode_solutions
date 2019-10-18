# Solution with Backtracking

import unittest


class Solution:
    def combinationSum2(self, candidates, target):
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
            if i > idx and nums[i]==nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)


class Test(unittest.TestCase):

    def test_combinationSum2(self):
        ans = Solution()
        self.assertCountEqual(ans.combinationSum2([2,3,6,7], 7), [[7]])
        self.assertCountEqual(ans.combinationSum2([], 0), [[]])
        self.assertCountEqual(ans.combinationSum2([2,3,5], 8), [[3,5]])
        self.assertCountEqual(ans.combinationSum2([2,3,6,7], 9), [[2,7],[3,6]])
        self.assertCountEqual(ans.combinationSum2([2,3,6,7], 1), [])
        self.assertCountEqual(ans.combinationSum2([10,1,2,7,6,1,5], 8), [[1,7],[1,2,5],[2,6],[1,1,6]])
        self.assertCountEqual(ans.combinationSum2([2,5,2,1,2], 5), [[1,2,2],[5]])

if __name__ == "__main__":

    unittest.main()
