# Simple Solution with Built-In Method

import unittest


def myAtoi(str):

    str = str.strip()

    if len(str) == 0:
        return 0

    res_str, res, i = "0", 0, 0

    if str[0] in "+-":
        res_str = str[0]
        i = 1

    for i in range(i, len(str)):
        if str[i].isdigit():
            res_str += str[i]
        else:
            break

    if len(res_str) > 1:
        res = int(res_str)

    if res > 2**31-1 > 0:
        return 2**31-1
    elif res < -2**31 < 0:
        return -2**31
    else:
        return res


class Test(unittest.TestCase):

    def test_myAtoi(self):
        self.assertEqual(myAtoi("42"), 42)
        self.assertEqual(myAtoi("   -42"), -42)
        self.assertEqual(myAtoi(" a -42"), 0)
        self.assertEqual(myAtoi("4193 with words"), 4193)
        self.assertEqual(myAtoi("words and 987"), 0)
        self.assertEqual(myAtoi("-91283472332"), -2147483648)
        self.assertEqual(myAtoi(""), 0)
        self.assertEqual(myAtoi(" "), 0)
        self.assertEqual(myAtoi("--42"), 0)
        self.assertEqual(myAtoi("+-42"), 0)
        self.assertEqual(myAtoi("4 2"), 4)
        self.assertEqual(myAtoi("4+2"), 4)

if __name__ == "__main__":

    unittest.main()
