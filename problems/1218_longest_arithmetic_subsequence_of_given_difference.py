# O(N) Solution with Dynamic Programming

import unittest


def longestSubsequence(arr, difference):
    dic = {}
    for num in arr:
        dic[num] = dic.get(num-difference, 0) + 1
    return max(dic.values())


class Test(unittest.TestCase):

    def test_longestSubsequence(self):
        self.assertEqual(longestSubsequence([1,2,3,4], 1), 4)
        self.assertEqual(longestSubsequence([1,3,5,7], 1), 1)
        self.assertEqual(longestSubsequence([1,5,7,8,5,3,4,2,1], -2), 4)
        self.assertEqual(longestSubsequence([1,1,1,1,1], 0), 5)
        self.assertEqual(longestSubsequence([1,1,0,1,1], 0), 4)
        self.assertEqual(longestSubsequence([1,2,5,1,2], 1), 2)


if __name__ == "__main__":

    unittest.main()
