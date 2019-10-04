# O(N) Solution with Built-In Method

import unittest

def reverseWords(s):
    return " ".join(s.strip().split()[::-1])


class Test(unittest.TestCase):

    def test_reverseWords(self):
        self.assertEqual(reverseWords("the sky is blue"), "blue is sky the")
        self.assertEqual(reverseWords("  hello world!  "), "world! hello")
        self.assertEqual(reverseWords("a good   example"), "example good a")
        self.assertEqual(reverseWords("1a good.com   example..."), "example... good.com 1a")
        self.assertEqual(reverseWords("1 2 3 "), "3 2 1")

if __name__ == "__main__":

    unittest.main()
