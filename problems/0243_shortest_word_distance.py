# O(N) Solution with Simple Approach

import unittest


def shortestDistance(words, word1, word2):
    last, res = -1, len(words)
    for i in range(len(words)):
        if words[i] in [word1, word2]:
            if last != -1 and words[i] != words[last]:
                res = min(res, i-last)
            last = i
    return res


class Test(unittest.TestCase):

    def test_shortestDistance(self):
        self.assertEqual(shortestDistance(["practice","makes","perfect","coding","makes"], "coding", "practice"), 3)
        self.assertEqual(shortestDistance(["practice","makes","perfect","coding","makes"], "makes", "practice"), 1)
        self.assertEqual(shortestDistance([], "coding", "practice"), 0)
        self.assertEqual(shortestDistance(["practice","makes","perfect","coding","makes","practice"], "coding", "practice"), 2)
        self.assertEqual(shortestDistance(["practice","Practice","Practice","coding","Practice"], "coding", "practice"), 3)

if __name__ == "__main__":

    unittest.main()
