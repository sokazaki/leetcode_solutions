# O(N) Solution with Bottom-Up Approach

import unittest


def climbStairs(n):
    if n == 1:
        return 1
    pre, cur = 1, 2
    for _ in range(2, n):
        pre, cur = cur, pre+cur
    return cur

class Test(unittest.TestCase):

    def test_climbStairs(self):
        self.assertEqual(climbStairs(1), 1)
        self.assertEqual(climbStairs(2), 2)
        self.assertEqual(climbStairs(5), 8)
        self.assertEqual(climbStairs(10), 89)
        self.assertEqual(climbStairs(40), 165580141)

if __name__ == "__main__":

    unittest.main()
