# O(N) Solution with Hash Map

import unittest

def canPermutePalindrome(s):

    dic = {}
    for ch in s:
        dic[ch] = dic.get(ch, 0) + 1

    return sum(v % 2 for v in dic.values()) <= 1


class Test(unittest.TestCase):

    def test_canPermutePalindrome(self):
        self.assertEqual(canPermutePalindrome("code"), False)
        self.assertEqual(canPermutePalindrome("-----"), True)
        self.assertEqual(canPermutePalindrome("-+-+-+-+-"), True)
        self.assertEqual(canPermutePalindrome("aab"), True)
        self.assertEqual(canPermutePalindrome(""), True)
        self.assertEqual(canPermutePalindrome("carerca"), True)


if __name__ == "__main__":

    unittest.main()
