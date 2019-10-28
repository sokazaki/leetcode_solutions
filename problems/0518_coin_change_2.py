# O(NM) Solution with Dynamic Programming

import unittest

def change(amount, coins):
    dp = [0] * (amount+1)
    dp[0] = 1

    for i in coins:
        for j in range(1, amount+1):
            if j >= i:
                dp[j] += dp[j-i]
    return dp[amount]

class Test(unittest.TestCase):

    def test_change(self):
        self.assertEqual(change(5, [1, 2, 5]), 4)
        self.assertEqual(change(3, [2]), 0)
        self.assertEqual(change(3, [3]), 1)
        self.assertEqual(change(3, [4]), 0)
        self.assertEqual(change(35, [1, 2, 3, 5, 7, 9, 11, 15]), 1644)


if __name__ == "__main__":

    unittest.main()
