# O(N^2) Solution with Two Pointers

import unittest

class Solution:
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            res = self.helper(s, i, i, res)
            res = self.helper(s, i, i+1, res)

        return res

    def helper(self, s, left, right, res):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1; right += 1
            res += 1
        return res


class Test(unittest.TestCase):

    def test_countSubstrings(self):
        ans = Solution()
        self.assertEqual(ans.countSubstrings("abc"), 3)
        self.assertEqual(ans.countSubstrings("aaa"), 6)
        self.assertEqual(ans.countSubstrings("abbbssdfffddddsdddsaaasddssssdfg"), 68)
        self.assertEqual(ans.countSubstrings(""), 0)
        self.assertEqual(ans.countSubstrings("a"), 1)

if __name__ == "__main__":

    unittest.main()
