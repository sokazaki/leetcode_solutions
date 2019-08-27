# O(NK**2) Solution with Simple Solution

import unittest

def palindromePairs(words):

    rev = {word[::-1]: i for i, word in enumerate(words)}
    res = []

    for i, word in enumerate(words):
        if word:
            for j in range(len(word)):
                l, r = word[:j], word[j:]

                if l in rev and i != rev[l] and r == r[::-1]:
                    res.append([i,rev[l]])

                if r in rev and i != rev[r] and l == l[::-1]:
                    res.append([rev[r],i])
        else:
            for j, word in enumerate(words):
                if i != j and word == word[::-1]:
                    res.append([i,j])
    return res


class Test(unittest.TestCase):

    def test_palindromePairs(self):
        self.assertCountEqual(palindromePairs(["abcd","dcba","lls","s","sssll"]), [[0,1],[1,0],[3,2],[2,4]] )
        self.assertCountEqual(palindromePairs(["bat","tab","cat"]), [[0,1],[1,0]])
        self.assertCountEqual(palindromePairs(["bat","tab","cat", ""]), [[0,1],[1,0]])
        self.assertCountEqual(palindromePairs(["","bat", "tab","cat"]), [[2,1],[1,2]])
        self.assertCountEqual(palindromePairs(["a",""]), [[0,1],[1,0]])
        self.assertCountEqual(palindromePairs([""]), [])


if __name__ == "__main__":

    unittest.main()
