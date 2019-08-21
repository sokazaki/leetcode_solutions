# O(N) Solution with Stack

import unittest

def decodeString(s):
    stack = []
    stack.append(["", 1])
    num = 0
    for ch in s:
        if ch.isdigit():
            num += int(ch)
        elif ch == '[':
            stack.append(["", num])
            num = 0
        elif ch == ']':
            st, k = stack.pop()
            stack[-1][0] += st*k
        else:
            stack[-1][0] += ch
    return stack[0][0]

class Test(unittest.TestCase):

    def test_decodeString(self):
        self.assertEqual(decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(decodeString("3[a2[c]]"), "accaccacc")
        self.assertEqual(decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(decodeString("1[]"), "")
        self.assertEqual(decodeString("10[]"), "")
        self.assertEqual(decodeString("0[abc]"), "")

if __name__ == "__main__":

    unittest.main()
