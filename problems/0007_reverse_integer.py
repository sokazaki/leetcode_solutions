# O(N) Solution with simple approach

import unittest

def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
        x = str(x)[1:]
    else:
        x = str(x)

    x = int(x[::-1]) * sign

    return 0 if x > 2**31-1 or x < -2**31 else x

class Test(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse(123), 321)
        self.assertEqual(reverse(-123), -321)
        self.assertEqual(reverse(120), 21)
        self.assertEqual(reverse(-150), -51)
        self.assertEqual(reverse(int(str(2**31-1)[::-1])), 2147483647)
        self.assertEqual(reverse(int(str(2**31)[::-1])), 0)
        self.assertEqual(reverse(int("-"+str(2**31)[::-1])), -2147483648)
        self.assertEqual(reverse(int("-"+str(2**31+1)[::-1])), 0)

if __name__ == "__main__":

    unittest.main()
