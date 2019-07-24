# O(N) Solution with simple approach

import unittest

def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
        x = str(x)[1:]
    else:
        x = str(x)

    x = int(x[::-1])

    return 0 if x > 2**31-1 else x * sign

class Test(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse(123), 321)
        self.assertEqual(reverse(-123), -321)
        self.assertEqual(reverse(120), 21)
        self.assertEqual(reverse(-150), -51)

if __name__ == "__main__":

    unittest.main()
