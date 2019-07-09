# O(N) Solution with HashMap

import unittest

def groupAnagrams(strs):
    d = {}
    for w in strs:
        key = str(sorted(w))
        d[key] = d.get(key, []) + [w]
    return list(d.values())

class Test(unittest.TestCase):

    def test_groupAnagrams(self):
        self.assertListEqual(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), [["eat","tea","ate"],["tan","nat"],["bat"]])
        self.assertListEqual(groupAnagrams(["eat", "tea", "tbn", "ate", "nat", "bat"]), [["eat","tea","ate"],["tbn"],["nat"],["bat"]])
        self.assertListEqual(groupAnagrams(["eat", "eat", "tbn", ]), [["eat","eat"],["tbn"]])

if __name__ == "__main__":

    unittest.main()
