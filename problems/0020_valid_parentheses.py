import unittest

def isValid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
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
