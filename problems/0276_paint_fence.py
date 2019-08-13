# O(N) Solution with Dynamic Programming

import unittest

def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k

    same, diff = k, k*(k-1)
    for i in range(3, n+1):
        same, diff = diff, (same+diff)*(k-1)

    return same + diff


class Test(unittest.TestCase):

    def test_numWays(self):
        self.assertEqual(numWays(3, 2), 6)
        self.assertEqual(numWays(0, 5), 0)
        self.assertEqual(numWays(11, 0), 0)
        self.assertEqual(numWays(1, 121), 121)
        self.assertEqual(numWays(9, 7), 35426160)

if __name__ == "__main__":

    unittest.main()
