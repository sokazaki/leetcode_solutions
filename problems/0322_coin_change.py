# O(NK) Solution with Dynamic Programming

import unittest

def coinChange(coins, amount):
    res = [float('inf')] * (amount+1)
    res[0] = 0

    for coin in coins:
        for i in range(len(res)):
            if coin <= i:
                res[i] = min(res[i-coin]+1, res[i])

    if res[amount] == float('inf'):
        return -1
    else:
        return res[amount]


class Test(unittest.TestCase):

    def test_coinChange(self):
        self.assertEqual(coinChange([1,2,5], 11), 3)
        self.assertEqual(coinChange([1,5,10,50,100,500,1000,5000,10000], 49565), 13)
        self.assertEqual(coinChange([2], 3), -1)
        self.assertEqual(coinChange([2], 2), 1)
        self.assertEqual(coinChange([2], 40), 20)

if __name__ == "__main__":

    unittest.main()
