# O(N) Solution with Simple Approach

import unittest
from collections import Counter

def minDominoRotations(A, B):

    same, countA, countB = Counter(), Counter(A), Counter(B)
    for a, b in zip(A, B):
        if a == b:
            same[a] += 1

    for i in range(1, 7):
        if countA[i] + countB[i] - same[i] == len(A):
            return min(countA[i], countB[i]) - same[i]
    return -1


class Test(unittest.TestCase):

    def test_minDominoRotations(self):
        self.assertEqual(minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]), 2)
        self.assertEqual(minDominoRotations([3,5,1,2,3],[3,6,3,3,4]), -1)
        self.assertEqual(minDominoRotations([2,1],[1,1]), 0)
        self.assertEqual(minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]), 2)
        self.assertEqual(minDominoRotations([2,1,2,4,2,2,5],[5,2,6,2,3,2,4]), -1)

if __name__ == "__main__":

    unittest.main()
