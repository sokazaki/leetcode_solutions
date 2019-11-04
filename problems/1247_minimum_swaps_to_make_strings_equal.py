# O(N) Solution with Simple Approach

import unittest

def minimumSwap(s1, s2):
    if ((s1+s2).count("x") % 2 == 1) or ((s1+s2).count("y") % 2 == 1):
        return -1

    res = 0
    cnt_x = 0
    cnt_y = 0
    for ch1, ch2 in zip(s1, s2):
        if ch1 != ch2:
            if ch1 == "x" and ch2 == "y":
                cnt_x += 1
                res += 1
            elif ch1 == "y" and ch2 == "x":
                cnt_y += 1
                res += 1

    return res - (cnt_x//2 + cnt_y//2)

class Test(unittest.TestCase):

    def test_minimumSwap(self):
        self.assertEqual(minimumSwap("xx", "yy"), 1)
        self.assertEqual(minimumSwap("xy", "yx"), 2)
        self.assertEqual(minimumSwap("xx", "xy"), -1)
        self.assertEqual(minimumSwap("xxyyxyxyxx", "xyyxyxxxyx"), 4)
        self.assertEqual(minimumSwap("xxxxyy", "yyyyxx"), 3)


if __name__ == "__main__":

    unittest.main()
