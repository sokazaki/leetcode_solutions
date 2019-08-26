# O(N) Time Complexity / O(1) Space Complexity Solution with Dynamic Programming

import unittest

def numDecodings(s):

    if not s or s[0] == '0':
        return 0

    dp1, dp2, cur = 1, 1, 0

    for i in range(1, len(s)):
        if '1' <= s[i] <= '9':
            cur = dp1
        if 10 <= int(s[i-1:i+1]) <= 26:
            cur += dp2
        dp1, dp2, cur = cur, dp1, 0

    return dp1


class Test(unittest.TestCase):

    def test_numDecodings(self):
        self.assertEqual(numDecodings("12"), 2)
        self.assertEqual(numDecodings("226"), 3)
        self.assertEqual(numDecodings("236"), 2)
        self.assertEqual(numDecodings("230"), 0)
        self.assertEqual(numDecodings("2310"), 2)
        self.assertEqual(numDecodings("2305"), 0)
        self.assertEqual(numDecodings("23105"), 2)
        self.assertEqual(numDecodings("99191199110"), 6)
        self.assertEqual(numDecodings("11111111111"), 144)

if __name__ == "__main__":

    unittest.main()
