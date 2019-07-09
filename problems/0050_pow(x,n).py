# O(logN) Solution with Bit Manipulation

import unittest

def myPow(x, n):
    if x==0 or n==0: return 1
    if n<0:
        x = 1.0/x
        n = -n
    k = 1
    while(n>1):
        if n % 2 != 0: k *= x
        x *= x
        n //= 2
    return k * x

class Test(unittest.TestCase):

    def test_myPow(self):
        self.assertAlmostEqual(myPow(2.00000,10), 1024.00000, places=7)
        self.assertAlmostEqual(myPow(2.10000,3), 9.26100, places=7)
        self.assertAlmostEqual(myPow(2.00000,-2), 0.25000, places=7)
        self.assertAlmostEqual(myPow(0,0), 1, places=7)
        self.assertAlmostEqual(myPow(0,1), 1, places=7)
        self.assertAlmostEqual(myPow(1,0), 1, places=7)

if __name__ == "__main__":

    unittest.main()
