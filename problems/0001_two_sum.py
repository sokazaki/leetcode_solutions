# O(N) Solution with HashMap
# (Another: O(N^2) Solution with Simple Brute-force loop)

import unittest

def twoSum(nums, target):
    remainder = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in remainder:
            return [remainder[m], i]
        else:
            remainder[n] = i

class Test(unittest.TestCase):

    def test_twoSum(self):
        self.assertListEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertListEqual(twoSum([2, 7, 11, 15], 26), [2, 3])
        self.assertListEqual(twoSum([2, 9], 11), [0, 1])
        self.assertListEqual(twoSum([-1, 4, 9], 8), [0, 2])


if __name__ == "__main__":

    unittest.main()
