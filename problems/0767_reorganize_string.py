# O(NlogN) Solution with Greedy

import unittest
from collections import Counter


def reorganizeString(S):
    if len(S)%2 == 0 and Counter(S).most_common()[0][1] >= len(S)//2 + 1:
        return ""
    if len(S)%2 == 1 and Counter(S).most_common()[0][1] >= len(S)//2 + 2:
        return ""

    res, stack = [0] * len(S) , ""
    for ch, cnt in Counter(S).most_common():
        stack += ch * cnt
    stack = list(stack)[::-1]

    i = 0
    while i <= len(res)-1:
        res[i] = stack.pop()
        i += 2
    i = 1
    while i <= len(res)-1:
        res[i] = stack.pop()
        i += 2

    return "".join(res)


class Test(unittest.TestCase):

    def test_reorganizeString(self):
        self.assertEqual(reorganizeString("aab"), "aba")
        self.assertEqual(reorganizeString("aaab"), "")
        self.assertEqual(reorganizeString("aaaab"), "")
        self.assertEqual(reorganizeString("aabbccddeeeeffff"), "eaeaebebfcfcfdfd")
        self.assertEqual(reorganizeString("aaaaabbbbbccddddeeeeffff"), "adadaeaeaebebfbfbfbfdcdc")
        self.assertEqual(reorganizeString("aaaaabbbbbccccddddeeeeeffff"), 'aeacacacacbdbdbdbdbfefefefe')

if __name__ == "__main__":

    unittest.main()
