# O(NM) Solution with Dynamic Programming

import unittest


def probabilityOfHeads(prob, target):
    n = len(prob)
    dp = [[0]*(target+1) for _ in range(n+1)]

    dp[0][0] = 1
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0]*(1-prob[i-1])

    for i in range(1, n+1):
        for j in range(1, target+1):
            dp[i][j] = dp[i-1][j-1]*prob[i-1] + dp[i-1][j]*(1-prob[i-1])

    return dp[n][target]


class Test(unittest.TestCase):

    def test_probabilityOfHeads(self):
        self.assertAlmostEqual(probabilityOfHeads([0.4], 1), 0.4)
        self.assertAlmostEqual(probabilityOfHeads([0.4], 0), 0.6)
        self.assertAlmostEqual(probabilityOfHeads([0.5,0.5,0.5,0.5,0.5], 0), 0.03125)
        self.assertAlmostEqual(probabilityOfHeads([0.3, 0.2, 0.15, 0.7, 0.49], 3), 0.19541)
        self.assertAlmostEqual(probabilityOfHeads([0.3, 0.2, 0.15, 0.7, 0.49], 4), 0.04158)


if __name__ == "__main__":

    unittest.main()
