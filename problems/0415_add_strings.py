# O(N) Solution with Simple Approach

import unittest

def addStrings(num1, num2):

    idict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

    i = len(num1)-1
    j = len(num2)-1
    carry = 0
    res = ''

    while i >= 0 or j >= 0:
        n1 = idict[num1[i]] if i >= 0 else 0
        n2 = idict[num2[j]] if j >= 0 else 0
        n = n1 + n2 + carry

        if n >= 10:
            carry = 1
            n -= 10
        else:
            carry = 0

        res = str(n) + res

        i -= 1
        j -= 1

    if carry == 1:
        res = "1" + res

    return res

class Test(unittest.TestCase):

    def test_addStrings(self):
        self.assertEqual(addStrings("0", "0"), "0")
        self.assertEqual(addStrings("512", "25"), "537")
        self.assertEqual(addStrings("4987", "578"), "5565")
        self.assertEqual(addStrings("999", "1"), "1000")
        self.assertEqual(addStrings("12132134334233423423515143662", "65349759215721521395729363462"), "77481893549954944819244507124")

if __name__ == "__main__":

    unittest.main()
