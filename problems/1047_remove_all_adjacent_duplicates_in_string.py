# O(N) Solution with Stack

import unittest

def removeDuplicates(S):
    res = []
    for ch in S:
        if len(res)==0 or res[-1]!=ch:
            res.append(ch)
        else:
            res.pop()

    return "".join(res)

class Test(unittest.TestCase):

    def test_removeDuplicates(self):
        self.assertEqual(removeDuplicates("abbaca"), "ca")
        self.assertEqual(removeDuplicates("abbassdca"), "dca")
        self.assertEqual(removeDuplicates("abbaaca"), "aca")
        self.assertEqual(removeDuplicates("a"), "a")

if __name__ == "__main__":

    unittest.main()
