# O(N) Solution with Built-In Method

import unittest

def detectCapitalUse(word):

    return word.isupper() or word.islower() or word.istitle()


class Test(unittest.TestCase):

    def test_detectCapitalUse(self):
        self.assertEqual(detectCapitalUse("Hello"), True)
        self.assertEqual(detectCapitalUse("here"), True)
        self.assertEqual(detectCapitalUse("LOVELY"), True)
        self.assertEqual(detectCapitalUse("aAa"), False)
        self.assertEqual(detectCapitalUse("a@a"), True)
        self.assertEqual(detectCapitalUse("LeetCode"), False)
        self.assertEqual(detectCapitalUse("Leetcode"), True)

if __name__ == "__main__":

    unittest.main()
