# O(N) Solution with Greedy Approach

import unittest

def maxProfit(prices):

    res = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            res += prices[i] - prices[i-1]

    return res


class Test(unittest.TestCase):

    def test_maxProfit(self):
        self.assertEqual(maxProfit([7,1,5,3,6,4]), 7)
        self.assertEqual(maxProfit([1,9,2,10,5]), 16)
        self.assertEqual(maxProfit([7,6,4,3,1]), 0)
        self.assertEqual(maxProfit([]), 0)
        self.assertEqual(maxProfit([7]), 0)
        self.assertEqual(maxProfit([1,7,8]), 7)

if __name__ == "__main__":

    unittest.main()
