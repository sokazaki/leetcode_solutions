# O(N) Solution with Stack

import unittest

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            num_minus1 = stack.pop()
            num_minus2 = stack.pop()
            if token == "+":
                stack.append(num_minus2 + num_minus1)
            elif token == "-":
                stack.append(num_minus2 - num_minus1)
            elif token == "*":
                stack.append(num_minus2 * num_minus1)
            elif token == "/":
                if abs(num_minus2) < abs(num_minus1):
                    stack.append(0)
                else:
                    if num_minus2 * num_minus1 < 0:
                        stack.append(-1 * (abs(num_minus2) // abs(num_minus1)))
                    else:
                        stack.append(abs(num_minus2) // abs(num_minus1))
        else:
            stack.append(int(token))

    return stack[0]


class Test(unittest.TestCase):

    def test_evalRPN(self):
        self.assertEqual(evalRPN(["2","1","+","3","*"]), 9)
        self.assertEqual(evalRPN(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
        self.assertEqual(evalRPN(["2","11","/"]), 0)
        self.assertEqual(evalRPN(["2","-11","/"]), 0)
        self.assertEqual(evalRPN(["-2","11","/"]), 0)
        self.assertEqual(evalRPN(["-2","-11","/"]), 0)
        self.assertEqual(evalRPN(["22","-5","/"]), -4)
        self.assertEqual(evalRPN(["-22","5","/"]), -4)
        self.assertEqual(evalRPN(["-22","-5","/"]), 4)

if __name__ == "__main__":

    unittest.main()
