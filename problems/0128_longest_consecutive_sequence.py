# O(N) Solution with Hashmap

import unittest


def longestConsecutive(nums):
    nums = set(nums)
    res = 0
    while nums:
        first = last = nums.pop()
        while first-1 in nums:
            first -= 1
            nums.remove(first)
        while last+1 in nums:
            last += 1
            nums.remove(last)
        res = max(res, last-first+1)

    return res


class Test(unittest.TestCase):

    def test_longestConsecutive(self):
        self.assertEqual(longestConsecutive([100,4,200,1,3,2]), 4)
        self.assertEqual(longestConsecutive([100,4,200,1,33,2]), 2)
        self.assertEqual(longestConsecutive([1,44,200,1,3,2]), 3)
        self.assertEqual(longestConsecutive([]), 0)
        self.assertEqual(longestConsecutive([100,44,200,11,33,2]), 1)

if __name__ == "__main__":

    unittest.main()
