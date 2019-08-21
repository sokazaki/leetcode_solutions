# O(N) Solution with Two Pointers

import unittest

def validPalindrome(s):

    i, j = 0, len(s)-1

    while i < j:
        if s[i] != s[j]:
            one, two = s[i:j], s[i+1:j+1]
            return one == one[::-1] or two == two[::-1]
        i += 1
        j -= 1

    return True


class Test(unittest.TestCase):

    def test_validPalindrome(self):
        self.assertEqual(validPalindrome("aba"), True)
        self.assertEqual(validPalindrome("abc"), False)
        self.assertEqual(validPalindrome("deeee"), True)
        self.assertEqual(validPalindrome("a"), True)
        self.assertEqual(validPalindrome("leetcode"), False)
        self.assertEqual(validPalindrome("carerac"), True)


if __name__ == "__main__":

    unittest.main()
