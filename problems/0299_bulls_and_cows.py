# O(N) Solution with Hash Map

import unittest
from collections import defaultdict


def getHint(secret, guess):
    secret_dic = defaultdict(int)
    guess_dic = defaultdict(int)

    bull, cow = 0, 0
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            bull += 1
        else:
            secret_dic[secret[i]] += 1
            guess_dic[guess[i]] += 1


    for ch in guess_dic:
        cow += min(guess_dic[ch], secret_dic[ch])

    return "{}A{}B".format(bull, cow)


class Test(unittest.TestCase):

    def test_getHint(self):
        self.assertEqual(getHint("1807", "7810"), "1A3B")
        self.assertEqual(getHint("1123", "0111"), "1A1B")
        self.assertEqual(getHint("11", "01"), "1A0B")
        self.assertEqual(getHint("11", "11"), "2A0B")
        self.assertEqual(getHint("12", "30"), "0A0B")

if __name__ == "__main__":

    unittest.main()
