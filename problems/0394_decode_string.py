import unittest

def decodeString(s):
    stack = []
    stack.append(["", 1])
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            stack.append(["", int(num)])
            num = ""
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

if __name__ == "__main__":

    unittest.main()
