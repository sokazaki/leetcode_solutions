# Solution with Backtracking

import unittest


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, idx, path, res):
        res.append(path)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)


class Test(unittest.TestCase):

    def test_subsetsWithDup(self):
        ans = Solution()
        self.assertCountEqual(ans.subsetsWithDup([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(ans.subsetsWithDup([]), [[]])
        self.assertCountEqual(ans.subsetsWithDup([3,1,2]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(ans.subsetsWithDup([3,6,1,7]), [[],[1],[1,3],[1,3,6],[1,3,6,7],[1,3,7],[1,6],[1,6,7],[1,7],[3],[3,6],[3,6,7],[3,7],[6],[6,7],[7]])
        self.assertCountEqual(ans.subsetsWithDup([1]), [[],[1]])
        self.assertCountEqual(ans.subsetsWithDup([1,2,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]])
        self.assertCountEqual(ans.subsetsWithDup([1,2,2,2]), [[],[1],[1,2],[1,2,2],[1,2,2,2],[2],[2,2],[2,2,2]])

if __name__ == "__main__":

    unittest.main()
