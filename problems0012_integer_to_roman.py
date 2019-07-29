# Solution with Hash Map

import unittest

def intToRoman(num):
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    res = ""

    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v

    return res



class Test(unittest.TestCase):

    def test_intToRoman(self):
        self.assertEqual(intToRoman(3), "III")
        self.assertEqual(intToRoman(4), "IV")
        self.assertEqual(intToRoman(9), "IX")
        self.assertEqual(intToRoman(58), "LVIII")
        self.assertEqual(intToRoman(999), "CMXCIX")
        self.assertEqual(intToRoman(1000), "M")
        self.assertEqual(intToRoman(3999), "MMMCMXCIX")

if __name__ == "__main__":

    unittest.main()
