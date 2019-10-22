# O(N) Solution with Two Pointers

import unittest
from collections import defaultdict


def minWindow(s, t):

    dic, min_len = defaultdict(int), len(s)+1
    for ch in t:
        dic[ch] += 1
    left = right = min_start = 0
    count = len(dic)

    while right < len(s):
        while count > 0 and right < len(s):
            dic[s[right]] -= 1
            if dic[s[right]] == 0:
                count -= 1
            right += 1
        while count == 0:
            dic[s[left]] += 1
            if dic[s[left]] == 1:
                count = 1
                if right - left < min_len:
                    min_len, min_start = right - left, left
            left += 1

    return s[min_start : min_start+min_len] if min_len != len(s)+1 else ''


class Test(unittest.TestCase):

    def test_minWindow(self):
        self.assertEqual(minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(minWindow("a", "aa"), "")
        self.assertEqual(minWindow("a", "a"), "a")
        self.assertEqual(minWindow("ADOBECODEBANC", "AABC"), "ADOBECODEBA")
        self.assertEqual(minWindow("CODEFORCESLEETCODE", "FODT"), "DEFORCESLEET")


if __name__ == "__main__":

    unittest.main()
