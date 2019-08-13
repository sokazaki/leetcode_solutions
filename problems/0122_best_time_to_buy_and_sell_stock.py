# O(N) Solution with Dynamic Programming

import unittest

def maxProfit(prices):
    res, min_price = 0, float('inf')

    for price in prices:
        res = max(res, price-min_price)
        min_price = min(min_price, price)

    return res


class Test(unittest.TestCase):

    def test_maxProfit(self):
        self.assertEqual(maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(maxProfit([7,6,4,3,1]), 0)
        self.assertEqual(maxProfit([]), 0)
        self.assertEqual(maxProfit([7]), 0)
        self.assertEqual(maxProfit([1,7,8]), 7)

if __name__ == "__main__":

    unittest.main()
