# O(N) Solution with Hash Set

import unittest


def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


class Test(unittest.TestCase):

    def test_isIsomorphic(self):
        self.assertEqual(isIsomorphic("egg", "add"), True)
        self.assertEqual(isIsomorphic("foo", "bar"), False)
        self.assertEqual(isIsomorphic("paper", "title"), True)
        self.assertEqual(isIsomorphic("ab", "aa"), False)
        self.assertEqual(isIsomorphic("abba", "abab"), False)

if __name__ == "__main__":

    unittest.main()
