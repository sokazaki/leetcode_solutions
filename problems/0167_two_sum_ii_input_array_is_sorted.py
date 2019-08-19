# O(N) Solution with HashMap
# (Another: O(N^2) Solution with Simple Brute-force loop)

import unittest

def twoSum(nums, target):
    rem = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in rem:
            return [rem[m]+1, i+1]
        else:
            rem[n] = i

class Test(unittest.TestCase):

    def test_twoSum(self):
        self.assertListEqual(twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertListEqual(twoSum([2, 7, 11, 15], 26), [3, 4])
        self.assertListEqual(twoSum([2, 9], 11), [1, 2])
        self.assertListEqual(twoSum([-1, 4, 9], 8), [1, 3])


if __name__ == "__main__":

    unittest.main()
