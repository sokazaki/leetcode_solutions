# O(N) Time Complexity / O(1) Space Complexity Solution with Two Pointers

import unittest

def compress(chars):
    left = cur = 0

    while cur < len(chars):
        char, count = chars[cur], 1
        while (cur+1) < len(chars) and char == chars[cur+1]:
            count, cur = count+1, cur+1
        chars[left] = char
        if count > 1:
            chars[left+1:left+1+len(str(count))] = str(count)
            left += len(str(count))
        left, cur = left+1, cur+1

    return chars[:left]


class Test(unittest.TestCase):

    def test_compress(self):
        self.assertEqual(compress(["a","a","b","b","c","c","c"]), ["a","2","b","2","c","3"])
        self.assertEqual(compress(["a","a","b","b","c","a","c"]), ["a","2","b","2","c","a","c"])
        self.assertEqual(compress(["a"]), ["a"])
        self.assertEqual(compress(["a","a"]), ["a","2"])
        self.assertEqual(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), ["a","b","1","2"])

if __name__ == "__main__":

    unittest.main()
