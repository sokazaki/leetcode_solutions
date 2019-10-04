# O(C) Solution with Simple Approach

import unittest
from collections import Counter

def isAnagram(s, t):
    return Counter(s)==Counter(t)


class Test(unittest.TestCase):

    def test_isAnagram(self):
        self.assertEqual(isAnagram("anagram", "nagaram"), True)
        self.assertEqual(isAnagram("rat", "car"), False)
        self.assertEqual(isAnagram("rar", "rar"), True)
        self.assertEqual(isAnagram("aa", "a"), False)
        self.assertEqual(isAnagram("", "a"), False)

if __name__ == "__main__":

    unittest.main()
