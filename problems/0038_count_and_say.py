# Solution with simple approach

import unittest

class Solution:
    def countAndSay(self, n):
        res = "1"
        for _ in range(n-1):
            res = self.helper(res)
        return res

    def helper(self, n):
        count, i, res = 1, 0, ""
        while i < len(n)-1:
            if n[i] == n[i+1]:
                count += 1
            else:
                res += str(count) + n[i]
                count = 1
            i += 1
        res += str(count) + n[i]

        return res

class Test(unittest.TestCase):

    def test_countAndSay(self):
        ans = Solution()
        self.assertEqual(ans.countAndSay(1), "1")
        self.assertEqual(ans.countAndSay(2), "11")
        self.assertEqual(ans.countAndSay(3), "21")
        self.assertEqual(ans.countAndSay(4), "1211")
        self.assertEqual(ans.countAndSay(5), "111221")
        self.assertEqual(ans.countAndSay(6), "312211")
        self.assertEqual(ans.countAndSay(10), "13211311123113112211")

if __name__ == "__main__":

    unittest.main()
