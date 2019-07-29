# Solution with Hash Map

import unittest

def romanToInt(s):
    dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
    res = 0

    i=0
    s = list(s)

    while i+1<=len(s)-1:
        if s[i]+s[i+1] in dic:
            res += dic[s[i]+s[i+1]]
            i += 2
        else:
            res += dic[s[i]]
            i += 1

    if i+1==len(s):
        return res+dic[s[i]]
    else:
        return res



class Test(unittest.TestCase):

    def test_romanToInt(self):
        self.assertEqual(romanToInt("III"), 3)
        self.assertEqual(romanToInt("IV"), 4)
        self.assertEqual(romanToInt("IX"), 9)
        self.assertEqual(romanToInt("LVIII"), 58)
        self.assertEqual(romanToInt("MCMXCIV"), 1994)

if __name__ == "__main__":

    unittest.main()
