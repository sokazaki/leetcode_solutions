# O(N) Solution with Two Pointer and Sliding Window
# (Another: O(N^2) Solution with Simple Brute-force approach)

import unittest

def characterReplacement(s, k):
    count = {}
    max_count = start = result = 0
    for i, c in enumerate(s):
        count[c] = count.get(c, 0) + 1
        max_count = max(max_count, count[c])
        if i - start + 1 - max_count > k:
            count[s[start]] -= 1
            start += 1
        result = max(result, i - start + 1)

    return result

class Test(unittest.TestCase):

    def test_characterReplacement(self):
        self.assertEqual(characterReplacement("ABAB",2), 4)
        self.assertEqual(characterReplacement("AABABBA",1), 4)
        self.assertEqual(characterReplacement("AAAAAAA",1), 7)
        self.assertEqual(characterReplacement("AAABAAA",1), 7)
        self.assertEqual(characterReplacement("",1), 0)
        self.assertEqual(characterReplacement("",0), 0)
        self.assertEqual(characterReplacement("A",0), 1)
        self.assertEqual(characterReplacement("AB",0), 1)


if __name__ == "__main__":

    unittest.main()
