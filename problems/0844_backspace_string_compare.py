import unittest

# O(N)/O(N) Solution with Stack
def backspaceCompare(S, T):
    s_stack = []
    t_stack = []
    for ch in S:
        if ch=="#" and s_stack:
            s_stack.pop()
        elif ch=="#":
            pass
        else:
            s_stack.append(ch)
    for ch in T:
        if ch=="#" and t_stack:
            t_stack.pop()
        elif ch=="#":
            pass
        else:
            t_stack.append(ch)
    if len(s_stack)!=len(t_stack):
        return False
    for i, j in zip(s_stack, t_stack):
        if i!=j:
            return False
    return True

# O(N)/O(1) Solution with Two Pointers
def backspaceCompare2(S, T):
    si, ti = len(S)-1, len(T)-1
    count_s = count_t = 0

    while si >= 0 or ti >= 0:

        while si >= 0:
            if S[si] == '#':
                count_s += 1
                si -= 1
            elif S[si] != '#' and count_s > 0:
                count_s -= 1
                si -= 1
            else:
                break

        while ti >= 0:
            if T[ti] == '#':
                count_t += 1
                ti -= 1
            elif T[ti] != '#' and count_t > 0:
                count_t -= 1
                ti -= 1
            else:
                break

        if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
            return False
        if (ti >= 0 and si >= 0) and S[si] != T[ti]:
            return False

        si -= 1
        ti -= 1

    return True


class Test(unittest.TestCase):

    def test_backspaceCompare(self):
        self.assertEqual(backspaceCompare("ab#c","ad#c"), True)
        self.assertEqual(backspaceCompare("ab##","c#d#"), True)
        self.assertEqual(backspaceCompare("a##c","#a#c"), True)
        self.assertEqual(backspaceCompare("a#c","b"), False)
        self.assertEqual(backspaceCompare("isfcow#","isfco#w#"), False)

    def test_backspaceCompare2(self):
        self.assertEqual(backspaceCompare2("ab#c","ad#c"), True)
        self.assertEqual(backspaceCompare2("ab##","c#d#"), True)
        self.assertEqual(backspaceCompare2("a##c","#a#c"), True)
        self.assertEqual(backspaceCompare2("a#c","b"), False)
        self.assertEqual(backspaceCompare2("isfcow#","isfco#w#"), False)

if __name__ == "__main__":

    unittest.main()
