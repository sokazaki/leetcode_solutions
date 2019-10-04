# O(N) Solution with Simple Approach

import unittest

def titleToNumber(s):
    res = 0
    for exp, char in enumerate(s):
        res += (ord(char) - 65 + 1) * (26 ** (len(s)-exp-1))
    return res


class Test(unittest.TestCase):

    def test_titleToNumber(self):
        self.assertEqual(titleToNumber("A"), 1)
        self.assertEqual(titleToNumber("AB"), 28)
        self.assertEqual(titleToNumber("ZY"), 701)
        self.assertEqual(titleToNumber("ZWA"), 18175)
        self.assertEqual(titleToNumber("LEETCODE"), 97994910369)

if __name__ == "__main__":

    unittest.main()
