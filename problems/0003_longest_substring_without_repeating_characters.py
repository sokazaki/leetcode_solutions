# O(N) Solution with Two Pointers and Sliding Window
# (Another: O(N^2) Solution with Simple Brute-force approach)

import unittest

def lengthOfLongestSubstring(s):

    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[c] = i


    return max_length

class Test(unittest.TestCase):

    def test_lengthOfLongestSubstring(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(lengthOfLongestSubstring("tmmzuxt"), 5)
        self.assertEqual(lengthOfLongestSubstring(""), 0)


if __name__ == "__main__":

    unittest.main()
