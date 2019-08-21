# O(N) Solution with Simple Approach

import unittest

def generatePossibleNextMoves(s):
    res = []
    count = 0
    i=0
    while i<=len(s)-2:
        if s[i] == s[i+1] == "+":
            res.append(s[:i]+"--"+s[i+2:])
            count = 1
        i+=1

    if count:
        return res
    else:
        return []


class Test(unittest.TestCase):

    def test_generatePossibleNextMoves(self):
        self.assertEqual(generatePossibleNextMoves("++++"), ["--++","+--+","++--"])
        self.assertEqual(generatePossibleNextMoves("-----"), [])
        self.assertEqual(generatePossibleNextMoves("-+-+-+-+-"), [])
        self.assertEqual(generatePossibleNextMoves("++"), ["--"])
        self.assertEqual(generatePossibleNextMoves("-++"), ["---"])


if __name__ == "__main__":

    unittest.main()
