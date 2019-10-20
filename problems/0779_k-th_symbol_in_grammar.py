# O(N) Solution with Recursion

import unittest


def kthGrammar(N, K):
    if N == 1 and K == 1:
        return 0
    if K%2 == 1:
        return kthGrammar(N-1, K//2 + K%2)
    else:
        return 1-kthGrammar(N-1, K//2 + K%2)


class Test(unittest.TestCase):

    def test_kthGrammar(self):
        self.assertEqual(kthGrammar(1,1), 0)
        self.assertEqual(kthGrammar(2,2), 1)
        self.assertEqual(kthGrammar(2,1), 0)
        self.assertEqual(kthGrammar(4,2), 1)
        self.assertEqual(kthGrammar(10,100), 0)
        self.assertEqual(kthGrammar(30,100), 0)
        self.assertEqual(kthGrammar(30,33554432), 1)
        self.assertEqual(kthGrammar(300,33554432000), 1)


if __name__ == "__main__":

    unittest.main()
