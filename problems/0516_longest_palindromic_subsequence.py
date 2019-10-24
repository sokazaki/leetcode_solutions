# O(N^2) Solution with Dynamic Programming

import unittest


def longestPalindromeSubseq(s):
    if s == s[::-1]:
        return len(s)
    dp = [[0]*len(s) for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    k = 1

    while k < len(s):
        for i in range(len(s)-k):
            j = i + k
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        k += 1

    return dp[0][len(s)-1]


class Test(unittest.TestCase):

    def test_longestPalindromeSubseq(self):
        self.assertEqual(longestPalindromeSubseq("bbbab"), 4)
        self.assertEqual(longestPalindromeSubseq("cbbd"), 2)
        self.assertEqual(longestPalindromeSubseq("asssddssddddsaasdsagg"), 14)
        self.assertEqual(longestPalindromeSubseq("asssddssddsdsdsdsaasaadsdsagg"), 19)
        self.assertEqual(longestPalindromeSubseq(""), 0)


if __name__ == "__main__":

    unittest.main()
