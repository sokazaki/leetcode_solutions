# Simple Solution with Math

import unittest


def multiply(num1, num2):
    res = 0
    for i, n1 in enumerate(num1[::-1]):
        tmp = int(n1) * (10**i)
        for j, n2 in enumerate(num2[::-1]):
            res += tmp * (int(n2) * (10**j))
    return str(res)


class Test(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply("2", "3"), "6")
        self.assertEqual(multiply("123", "456"), "56088")
        self.assertEqual(multiply("123", "0"), "0")
        self.assertEqual(multiply("1234", "1456"), "1796704")
        self.assertEqual(multiply("1230", "456"), "560880")

if __name__ == "__main__":

    unittest.main()
