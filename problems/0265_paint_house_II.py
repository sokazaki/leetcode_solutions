# O(NK) Solution with Dynamic Programming

import unittest

def minCostII(costs):

    if not costs:
        return 0

    dp = costs[0]
    for i in range(1, len(costs)):
        next_dp = [0]* len(costs[0])
        for k in range(len(costs[0])):
            next_dp[k] = costs[i][k] + min(dp[:k]+dp[k+1:])

        dp = next_dp

    return min(dp)


class Test(unittest.TestCase):

    def test_minCostII(self):
        self.assertEqual(minCostII([[17,2,17,99],[16,16,5,2],[14,3,19,55]]), 7)
        self.assertEqual(minCostII([]), 0)
        self.assertEqual(minCostII([[17,2,17],[16,16,5],[14,3,19], [2,5,1], [3,77,1]]), 13)
        self.assertEqual(minCostII([[17,2,17],[16,16,5],[14,3,19], [2,5,1], [3,77,1], [33,5,111]]), 18)
        self.assertEqual(minCostII([[17,2,17],[16,16,5],[14,3,19], [2,5,1], [3,77,1], [333,5555,111]]), 125)

if __name__ == "__main__":

    unittest.main()
