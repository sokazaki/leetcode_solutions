# O(NL) Solution with Dynamic Programming

import unittest


def wordBreak(s, wordDict):

    dp = [False for _ in range(len(s)+1)]
    dp[0] = True

    for i in range(1, len(s)+1):
        for w in wordDict:
            if dp[i-len(w)] and s[i-len(w):i]==w:
                dp[i]=True

    return dp[-1]


class Test(unittest.TestCase):

    def test_wordBreak(self):
        self.assertEqual(wordBreak("leetcode", ["leet", "code"]), True)
        self.assertEqual(wordBreak("applepenapple", ["apple", "pen"]), True)
        self.assertEqual(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
        self.assertEqual(wordBreak("catsandog", ["cats", "dog", "sand", "an", "cat"]), True)
        self.assertEqual(wordBreak("", ["leet", "code"]), True)

if __name__ == "__main__":

    unittest.main()
