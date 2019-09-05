# O(N) Solution with Dynamic Programming

import unittest

def fib(N):
    dp = [0]*(N+1)
    if N==0:
        return 0
    if N==1:
        return 1
    dp[1] = 1
    for i in range(2, N+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[N]


class Test(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(30), 832040)


if __name__ == "__main__":

    unittest.main()
