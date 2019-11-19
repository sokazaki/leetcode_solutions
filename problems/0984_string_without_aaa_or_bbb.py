# Simple Solution with Greedy

import unittest


def strWithout3a3b(A, B):
    if A+B<=3:
        return 'a' * A + 'b' * B

    if A >= 2*B:
        return 'aab'* B + 'a'* (A-2*B)
    elif A >= B:
        return 'aab' * (A-B) + 'ab' * (2*B - A)
    elif B >= 2*A:
        return 'bba' * A + 'b' *(B-2*A)
    else:
        return 'bba' * (B-A) + 'ab' * (2*A - B)


class Test(unittest.TestCase):

    def test_strWithout3a3b(self):
        self.assertEqual(strWithout3a3b(1, 2), "abb")
        self.assertEqual(strWithout3a3b(4, 1), "aabaa")
        self.assertEqual(strWithout3a3b(5, 7), "bbabbaababab")
        self.assertEqual(strWithout3a3b(7, 5), "aabaabababab")
        self.assertEqual(strWithout3a3b(3, 7), "bbabbabbab")

if __name__ == "__main__":

    unittest.main()
