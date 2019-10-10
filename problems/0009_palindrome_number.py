# O(N) Solution with Simple Approach

import unittest


def isPalindrome(x):
    if x < 0:
        return False
    p, res = x, 0
    while p:
        res = res * 10 + p % 10
        p = p // 10
    return res == x


class Test(unittest.TestCase):

    def test_isPalindrome(self):
        self.assertEqual(isPalindrome(121), True)
        self.assertEqual(isPalindrome(-121), False)
        self.assertEqual(isPalindrome(10), False)
        self.assertEqual(isPalindrome(1001), True)
        self.assertEqual(isPalindrome(664545466), True)

if __name__ == "__main__":

    unittest.main()
