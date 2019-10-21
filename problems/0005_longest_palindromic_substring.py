# O(N^2) Solution with Two Pointers

import unittest


class Solution:
    def longestPalindrome(self, s):
        res = ""

        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp

        return res

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1; right += 1
        return s[left+1:right]


class Test(unittest.TestCase):

    def test_longestPalindrome(self):
        ans = Solution()
        self.assertEqual(ans.longestPalindrome("babad"), "bab")
        self.assertEqual(ans.longestPalindrome("cbbd"), "bb")
        self.assertEqual(ans.longestPalindrome("babadddas"), "addda")
        self.assertEqual(ans.longestPalindrome(""), "")
        self.assertEqual(ans.longestPalindrome("b"), "b")


if __name__ == "__main__":

    unittest.main()
