# O(N) Solution with Stack

import unittest

def reverseParentheses(s):
    stack = []
    stack.append("")
    for ch in s:
        if ch == '(':
            stack.append("")
        elif ch == ')':
            st = stack.pop()
            stack[-1] += ''.join(list(reversed(st)))
        else:
            stack[-1] += ch
    return stack[0]

class Test(unittest.TestCase):

    def test_reverseParentheses(self):
        self.assertEqual(reverseParentheses("(abcd)"), "dcba")
        self.assertEqual(reverseParentheses("(u(love)i)"), "iloveu")
        self.assertEqual(reverseParentheses("(ed(et(oc))el)"), "leetcode")
        self.assertEqual(reverseParentheses("a(bcdefghijkl(mno)p)q"), "apmnolkjihgfedcbq")
        self.assertEqual(reverseParentheses("(ab)(cd)"), "badc")

if __name__ == "__main__":

    unittest.main()
