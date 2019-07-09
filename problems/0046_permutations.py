# O(N!) Solution with Built-In Function or Backtracking

import unittest
import collections
import itertools

class Solution:

    def permute(self, nums):
        return list(itertools.permutations(nums))


    def dfs(self, end_len, path, recoder):
        if len(path) == end_len:
            self.res.append(path)
        else:
            for key in recoder:
                if recoder[key] > 0:
                    recoder[key] -= 1
                    self.dfs(end_len, path+[key], recoder)
                    recoder[key] += 1


    def permute2(self, nums):
        recoder = collections.Counter(nums)
        self.res = []
        self.dfs(len(nums), [], recoder)
        return self.res

class Test(unittest.TestCase):

    def test_permute(self):
        ans = Solution()
        self.assertListEqual(sorted(ans.permute([1,2,3])), sorted([(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]))
        self.assertListEqual(sorted(ans.permute([1,2])), sorted([(1,2),(2,1)]))
        self.assertListEqual(sorted(ans.permute([1])), sorted([(1,)]))

    def test_permute2(self):
        ans = Solution()
        self.assertListEqual(sorted(ans.permute2([1,2,3])), sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]))
        self.assertListEqual(sorted(ans.permute2([1,2])), sorted([[1,2],[2,1]]))
        self.assertListEqual(sorted(ans.permute2([1])), sorted([[1]]))

if __name__ == "__main__":

    unittest.main()
