# O(NlogN) Time Complexity / O(N) Space Complexity Solution with Dynamic Programming

import unittest

def longestStrChain(words):
    dp = {}
    for w in sorted(words, key=len):
        dp[w] = max(dp.get(w[:i]+w[i+1:], 0) + 1 for i in range(len(w)))
    return max(dp.values())


class Test(unittest.TestCase):

    def test_longestStrChain(self):
        self.assertEqual(longestStrChain(["a","b","ba","bca","bda","bdca"]), 4)
        self.assertEqual(longestStrChain(["ba","b","a","bca","bda","bdca"]), 4)
        self.assertEqual(longestStrChain(["a","b","c","dd"]), 1)
        self.assertEqual(longestStrChain(["a","b","c","bb"]), 2)
        self.assertEqual(longestStrChain(["a","a","a","a"]), 1)

if __name__ == "__main__":

    unittest.main()
