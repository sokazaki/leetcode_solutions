# O(N) Solution with simple approach

import unittest

def longestCommonPrefix(strs):
    res = ''

    for x in zip(*strs):
        letters = set(x)
        if len(letters) == 1:
            res +=letters.pop()
        else:
            break

    return res

class Test(unittest.TestCase):

    def test_longestCommonPrefix(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl")
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]), "")
        self.assertEqual(longestCommonPrefix(["dog","dracecar","dcar"]), "d")
        self.assertEqual(longestCommonPrefix(["dog","dogo","dogg"]), "dog")

if __name__ == "__main__":

    unittest.main()
