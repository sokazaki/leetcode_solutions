# O(NloglogN) Solution with Sieve of Eratosthenes

import unittest

def countPrimes(n):
    sieve = [True for _ in range(n)]
    i = 2
    while i * i <= n-1:
        if sieve[i]:
            j = i + i
            while j <= n-1:
                sieve[j] = False
                j += i
        i += 1

    table = [i for i in range(n) if sieve[i] and i >= 2]
    return len(table)

class Test(unittest.TestCase):

    def test_countPrimes(self):
        self.assertEqual(countPrimes(10), 4)
        self.assertEqual(countPrimes(55), 16)
        self.assertEqual(countPrimes(112343), 10654)
        self.assertEqual(countPrimes(2), 0)
        self.assertEqual(countPrimes(3), 1)
        self.assertEqual(countPrimes(4), 2)
        self.assertEqual(countPrimes(5), 2)

if __name__ == "__main__":

    unittest.main()
