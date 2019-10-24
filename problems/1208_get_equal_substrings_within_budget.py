# O(N) Solution with Two Pointers

import unittest


def equalSubstring(s, t, maxCost):

    res, left, cost = 0, 0, 0
    for right in range(len(s)):
        cost += abs(ord(s[right]) - ord(t[right]))
        while cost > maxCost:
            cost -= abs(ord(s[left]) - ord(t[left]))
            left += 1
        res = max(res, right-left+1)

    return res


class Test(unittest.TestCase):

    def test_equalSubstring(self):
        self.assertEqual(equalSubstring("abcd", "bcdf", 3), 3)
        self.assertEqual(equalSubstring("abcd", "cdef", 3), 1)
        self.assertEqual(equalSubstring("abcd", "acde", 0), 1)
        self.assertEqual(equalSubstring("abcdcfsca", "bcdffdccv", 13), 6)
        self.assertEqual(equalSubstring("abcdcfscarfdxcsfa", "bcdffdccvdvdxcfsa", 27), 8)


if __name__ == "__main__":

    unittest.main()
