# O(N) Solution with Simple Approach

import unittest

def minRemoveToMakeValid(s):
    tmp = []
    cnt = 0
    for ch in s:
        if ch.isalpha():
            tmp.append(ch)
        elif ch == "(":
            tmp.append(ch)
            cnt += 1
        elif ch == ")" and cnt>=1:
            tmp.append(ch)
            cnt -= 1

    res = []
    cnt = 0
    for ch in tmp[::-1]:
        if ch.isalpha():
            res.append(ch)
        elif ch == ")":
            res.append(ch)
            cnt += 1
        elif ch == "(" and cnt>=1:
            res.append(ch)
            cnt -= 1

    return "".join(res[::-1])

class Test(unittest.TestCase):

    def test_minRemoveToMakeValid(self):
        self.assertEqual(minRemoveToMakeValid("lee(t(c)o)de)"), "lee(t(c)o)de")
        self.assertEqual(minRemoveToMakeValid("a)b(c)d"), "ab(c)d")
        self.assertEqual(minRemoveToMakeValid("))(("), "")
        self.assertEqual(minRemoveToMakeValid(""), "")
        self.assertEqual(minRemoveToMakeValid("xxxxyy"), "xxxxyy")

if __name__ == "__main__":

    unittest.main()
