# O(N) Solution with Simple Approach

import unittest

def fractionToDecimal(numerator, denominator):

    n, rem = divmod(abs(numerator), abs(denominator))
    sign = '-' if numerator*denominator < 0 else ''
    res = [sign+str(n), '.']
    remlist = []

    while rem not in remlist:
        remlist.append(rem)
        n, rem = divmod(rem*10, abs(denominator))
        res.append(str(n))

    idx = remlist.index(rem)
    res.insert(idx+2, '(')
    res.append(')')

    return ''.join(res).replace('(0)', '').rstrip('.')


class Test(unittest.TestCase):

    def test_fractionToDecimal(self):
        self.assertEqual(fractionToDecimal(1,2), "0.5")
        self.assertEqual(fractionToDecimal(2,1), "2")
        self.assertEqual(fractionToDecimal(2,3), "0.(6)")
        self.assertEqual(fractionToDecimal(4,9), "0.(4)")
        self.assertEqual(fractionToDecimal(4,333), "0.(012)")

if __name__ == "__main__":

    unittest.main()
