# O(N*2^N) Solution with Bit Manipulation or Backtracking

import unittest

# Bit Manipulation
def subsets(nums):
    res = []
    for i in range(2**len(nums)):
        tmp = []
        for bit_idx in range(len(nums)):
            if (i >> bit_idx) & 1 == 1:
                tmp.append(nums[bit_idx])
        res.append(tmp)

    return res

# Baktracking
class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, idx, path, res):
        res.append(path)
        for i in range(idx, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)


class Test(unittest.TestCase):

    # for Bit Manipulation
    def test_subsets(self):
        self.assertCountEqual(subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEquall(subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])

    # for Backtracking
    def test_subsets(self):
        ans = Solution()
        self.assertCountEqual(ans.subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(ans.subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(ans.subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(ans.subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertCountEqual(ans.subsets([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])

if __name__ == "__main__":

    unittest.main()
