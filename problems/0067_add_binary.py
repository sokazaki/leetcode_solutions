# O(N) Solution with Recursive

import unittest

class Solution:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1],b[:-1])+'0'
        else:
            return self.addBinary(a[:-1],b[:-1])+'1'

class Test(unittest.TestCase):

    def test_addBinary(self):
        ans = Solution()
        self.assertEqual(ans.addBinary("11","1"), "100")
        self.assertEqual(ans.addBinary("1010","1011"), "10101")
        self.assertEqual(ans.addBinary("0","0"), "0")
        self.assertEqual(ans.addBinary("1111","1111"), "11110")

if __name__ == "__main__":

    unittest.main()
