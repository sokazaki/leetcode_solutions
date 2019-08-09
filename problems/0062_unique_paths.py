# Simple Solution with Math

import unittest
import math

def uniquePaths(m, n):

    return int(math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1)))

class Test(unittest.TestCase):

    def test_uniquePaths(self):
        self.assertEqual(uniquePaths(3, 2), 3)
        self.assertEqual(uniquePaths(7, 3), 28)
        self.assertEqual(uniquePaths(1, 1), 1)
        self.assertEqual(uniquePaths(15, 15), 40116600)

if __name__ == "__main__":

    unittest.main()
