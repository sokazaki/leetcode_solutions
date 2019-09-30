# O(N) Solution with Simple Approach

import unittest

def isAlienSorted(words, order):

    order_idx = {word: i for i, word in enumerate(order)}
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if order_idx[word1[j]] > order_idx[word2[j]]:
                    return False
                break
            if j == min(len(word1), len(word2))-1 and len(word1) > len(word2):
                return False

    return True


class Test(unittest.TestCase):

    def test_isAlienSorted(self):
        self.assertEqual(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
        self.assertEqual(isAlienSorted(["hallo","hell","hello"], "hlabcdefgijkmnopqrstuvwxyz"), True)
        self.assertEqual(isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"), False)
        self.assertEqual(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(isAlienSorted(["app","apple"], "abcdefghijklmnopqrstuvwxyz"), True)


if __name__ == "__main__":

    unittest.main()
