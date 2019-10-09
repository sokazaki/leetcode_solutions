# O(NM) Solution with Brute Force
# (There are other solutions like Boyer-Moore, Knuth-Morris-Pratt, but they are practically slow.)

import unittest


def strStr(haystack, needle):
    for i in range(0, len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1


class Test(unittest.TestCase):

    def test_strStr(self):
        self.assertEqual(strStr("hello", "ll"), 2)
        self.assertEqual(strStr("aaaaa", "bba"), -1)
        self.assertEqual(strStr("aaaa", ""), 0)
        self.assertEqual(strStr("hellohello", "hell"), 0)
        self.assertEqual(strStr("", "bba"), -1)

if __name__ == "__main__":

    unittest.main()
