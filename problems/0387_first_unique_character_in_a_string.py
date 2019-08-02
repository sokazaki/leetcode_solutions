# O(N) Solution with Hash Map

import unittest
from collections import defaultdict

def firstUniqChar(s):
    d = defaultdict(int)

    for ch in s:
        d[ch] += 1

    for i, ch in enumerate(s):
        if d[ch]==1:
            return i
        else:
            continue

    return -1


class Test(unittest.TestCase):

    def test_firstUniqChar(self):
        self.assertEqual(firstUniqChar("leetcode"), 0)
        self.assertEqual(firstUniqChar("loveleetcode"), 2)
        self.assertEqual(firstUniqChar("lovelovevenetiansnares"), 12)
        self.assertEqual(firstUniqChar("ll"), -1)
        self.assertEqual(firstUniqChar(""), -1)

if __name__ == "__main__":

    unittest.main()
