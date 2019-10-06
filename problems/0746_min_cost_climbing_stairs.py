# O(N) Solution with Dynamic Programming

import unittest


def minCostClimbingStairs(cost):
    dp = [0]*len(cost)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, len(cost)):
        dp[i] = cost[i]+ min(dp[i-1], dp[i-2])
    return min(dp[len(cost)-1], dp[len(cost)-2])


class Test(unittest.TestCase):

    def test_findWords(self):
        self.assertEqual(minCostClimbingStairs([0,0,0,0]), 0)
        self.assertEqual(minCostClimbingStairs([10,15,20]), 15)
        self.assertEqual(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]), 6)
        self.assertEqual(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,100]), 104)
        self.assertEqual(minCostClimbingStairs([0,0]), 0)

if __name__ == "__main__":

    unittest.main()
