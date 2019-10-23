# O(N) Solution with Dynamic Programming

import unittest


def dieSimulator(n, rollMax):
    dp = [[0] * x for x in rollMax]
    for i in range(6):
        dp[i][0] = 1

    for _ in range(1, n):
        tmp = [[0] * x for x in rollMax]
        one_die_sum = [sum(x) for x in dp]
        total = sum(one_die_sum)
        for i in range(6):
            for j in range(rollMax[i]):
                if j == 0:
                    tmp[i][j] = (total - one_die_sum[i]) % (10**9 + 7)
                else:
                    tmp[i][j] = dp[i][j-1] % (10**9 + 7)
        dp = tmp

    return sum([sum(x) for x in dp]) % (10**9 + 7)

class Test(unittest.TestCase):

    def test_dieSimulator(self):
        self.assertEqual(dieSimulator(2, [1,1,2,2,2,3]), 34)
        self.assertEqual(dieSimulator(2, [1,1,1,1,1,1]), 30)
        self.assertEqual(dieSimulator(3, [1,1,1,2,2,3]), 181)
        self.assertEqual(dieSimulator(15, [1,1,2,2,2,3]), 275348769)
        self.assertEqual(dieSimulator(5000, [10,2,5,12,2,13]), 780435261)


if __name__ == "__main__":

    unittest.main()
