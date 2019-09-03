# O(N) Solution with Simple Approach

import unittest

def isNumber(s):

    s = s.strip()
    met_dot = met_e = met_digit = False

    for i, ch in enumerate(s):

        if ch in ['+', '-']:
            if i > 0 and s[i-1] != 'e':
                return False

        elif ch == '.':
            if met_dot or met_e:
                return False
            met_dot = True

        elif ch == 'e':
            if met_e or not met_digit:
                return False
            met_e, met_digit = True, False

        elif ch.isdigit():
            met_digit = True

        else:
            return False

    return met_digit

class Test(unittest.TestCase):

    def test_isNumber(self):
        self.assertEqual(isNumber("0"), True)
        self.assertEqual(isNumber(" 005047e+6"), True)
        self.assertEqual(isNumber(" 0.1 "), True)
        self.assertEqual(isNumber("abc"), False)
        self.assertEqual(isNumber("1 a"), False)
        self.assertEqual(isNumber("2e10"), True)
        self.assertEqual(isNumber(" -90e3   "), True)
        self.assertEqual(isNumber(" 1e"), False)
        self.assertEqual(isNumber("e3"), False)
        self.assertEqual(isNumber(" 6e-1"), True)
        self.assertEqual(isNumber(" 99e2.5 "), False)
        self.assertEqual(isNumber("53.5e93"), True)
        self.assertEqual(isNumber(" --6 "), False)
        self.assertEqual(isNumber("-+3"), False)
        self.assertEqual(isNumber("95a54e53"), False)


if __name__ == "__main__":

    unittest.main()
