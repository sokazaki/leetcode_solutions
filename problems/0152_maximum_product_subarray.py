# O(N) Time Complexity / O(1) Space Complexity Solution with Dynamic Programming

import unittest

def maxProduct(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    pos = neg = 0
    res = nums[0]
    for n in nums:
        if n > 0:
            pos, neg = max(n, n*pos), min(n, n*neg)
        else:
            pos, neg = max(n, n*neg), min(n, n*pos)
        res = max(pos, res)

    return res


class Test(unittest.TestCase):

    def test_maxProduct(self):
        self.assertEqual(maxProduct([2,3,-2,4]), 6)
        self.assertEqual(maxProduct([-2,0,-1]), 0)
        self.assertEqual(maxProduct([-2,5,-1]), 10)
        self.assertEqual(maxProduct([-2]), -2)

if __name__ == "__main__":

    unittest.main()
