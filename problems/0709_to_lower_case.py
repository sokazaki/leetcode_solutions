# O(N) Solution with Simple Approach

import unittest

def toLowerCase(str):

    return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)


class Test(unittest.TestCase):

    def test_toLowerCase(self):
        self.assertEqual(toLowerCase("Hello"), "hello")
        self.assertEqual(toLowerCase("here"), "here")
        self.assertEqual(toLowerCase("LOVELY"), "lovely")
        self.assertEqual(toLowerCase("aA@"), "aa@")
        self.assertEqual(toLowerCase("LeetCode"), "leetcode")

if __name__ == "__main__":

    unittest.main()
