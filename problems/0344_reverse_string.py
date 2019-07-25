# O(N) Solution with Two Pointers

import unittest

def reverseString(s):

    i, j = 0, len(s)-1

    while i<j:
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1

    return s


class Test(unittest.TestCase):

    def test_reverseString(self):
        self.assertListEqual(reverseString(["h","e","l","l","o"]), ["o","l","l","e","h"])
        self.assertListEqual(reverseString(["H","a","n","n","a","h"]), ["h","a","n","n","a","H"])
        self.assertListEqual(reverseString([]), [])

if __name__ == "__main__":

    unittest.main()
