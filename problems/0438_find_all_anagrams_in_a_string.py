# O(N) Solution with Hashmap + Sliding Window

import unittest
from collections import Counter

def findAnagrams(s, p):
    if len(p) > len(s):
        return []
    cnt_p = [0]*26
    cnt_s = [0]*26
    for ch in p:
        cnt_p[ord(ch)-ord("a")]+=1
    for i, ch in enumerate(s):
        cnt_s[ord(ch)-ord("a")]+=1
        if i == len(p)-1:
            break

    i, res = 0, []
    while True:
        if cnt_p==cnt_s:
            res.append(i)
        if i+len(p)>=len(s):
            break
        cnt_s[ord(s[i])-ord("a")] -= 1
        cnt_s[ord(s[i+len(p)])-ord("a")] += 1
        i+=1

    return res


class Test(unittest.TestCase):

    def test_findAnagrams(self):
        self.assertEqual(findAnagrams("cbaebabacd", "abc"), [0, 6])
        self.assertEqual(findAnagrams("abab", "ab"), [0, 1, 2])
        self.assertEqual(findAnagrams("abab", "abba"), [0])
        self.assertEqual(findAnagrams("abab", "abbaa"), [])
        self.assertEqual(findAnagrams("cbaebabacd", "aec"), [])

if __name__ == "__main__":

    unittest.main()
