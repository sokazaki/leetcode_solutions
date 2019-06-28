import unittest

def isValid(s):
    stack = []
    dic = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if stack == [] or dic[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

class Test(unittest.TestCase):

    def test_isValid(self):
        self.assertEqual(isValid(""), True)
        self.assertEqual(isValid("()"), True)
        self.assertEqual(isValid("()[]{}"), True)
        self.assertEqual(isValid("(]"), False)
        self.assertEqual(isValid("([)]"), False)
        self.assertEqual(isValid("{[]}"), True)
        self.assertEqual(isValid("{[]}()"), True)

if __name__ == "__main__":

    unittest.main()
