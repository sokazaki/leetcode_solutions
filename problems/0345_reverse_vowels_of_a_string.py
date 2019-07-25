# O(N) Solution with Two Pointers

import unittest

def reverseVowels(s):
    vowels = "aeiouAEIOU"
    idx = [i for i,j in enumerate(s) if j in vowels]
    s = list(s)
    i, j = 0, len(idx)-1

    while i<j:
        s[idx[i]], s[idx[j]] = s[idx[j]], s[idx[i]]
        i += 1
        j -= 1

    return "".join(s)


class Test(unittest.TestCase):

    def test_reverseVowels(self):
        self.assertEqual(reverseVowels("hello"), "holle")
        self.assertEqual(reverseVowels("leetcode"), "leotcede")
        self.assertEqual(reverseVowels("aA"), "Aa")
        self.assertEqual(reverseVowels("aAb"), "Aab")
        self.assertEqual(reverseVowels(""), "")

if __name__ == "__main__":

    unittest.main()
