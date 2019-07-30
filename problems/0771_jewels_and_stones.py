# O(N) Solution with Simple Approach

import unittest

def numJewelsInStones(J, S):

    res = 0
    for ch in S:
        if ch in J: res+=1

    return res


class Test(unittest.TestCase):

    def test_numJewelsInStones(self):
        self.assertEqual(numJewelsInStones("aA", "aAAbbbb"), 3)
        self.assertEqual(numJewelsInStones("z", "ZZ"), 0)
        self.assertEqual(numJewelsInStones("Z", "ZZ"), 2)
        self.assertEqual(numJewelsInStones("", "ZZ"), 0)
        self.assertEqual(numJewelsInStones("z", ""), 0)
        self.assertEqual(numJewelsInStones("", ""), 0)

if __name__ == "__main__":

    unittest.main()
