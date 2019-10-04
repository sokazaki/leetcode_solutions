# O(NC) Solution with Simple Approach

import unittest
from collections import Counter

def commonChars(A):
    res = Counter(A[0])
    for a in A:
        res &= Counter(a)
    return res.elements()


class Test(unittest.TestCase):

    def test_commonChars(self):
        self.assertCountEqual(commonChars(["bella","label","roller"]), ["e","l","l"])
        self.assertCountEqual(commonChars(["cool","lock","cook"]), ["c","o"])
        self.assertCountEqual(commonChars(["cool","loock","cook"]), ["c","o","o"])
        self.assertCountEqual(commonChars(["bella"]), ["a","b","e","l","l"])
        self.assertCountEqual(commonChars(["b"]), ["b"])

if __name__ == "__main__":

    unittest.main()
