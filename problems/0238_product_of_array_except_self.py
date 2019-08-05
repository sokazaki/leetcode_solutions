# O(N) Time Complexity / O(1) Space Complexity Solution with Simple Approach

import unittest

def productExceptSelf(nums):

    n = len(nums)
    res = []

    p = 1
    for i in range(n):
        res.append(p)
        p = p * nums[i]

    p = 1
    for i in range(n-1,-1,-1):
        res[i] = res[i] * p
        p = p * nums[i]

    return res


class Test(unittest.TestCase):

    def test_productExceptSelf(self):
        self.assertListEqual(productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertListEqual(productExceptSelf([24,12,8,6]), [576,1152,1728,2304])
        self.assertListEqual(productExceptSelf([1,0]), [0,1])
        self.assertListEqual(productExceptSelf([1,5]), [5,1])
        self.assertListEqual(productExceptSelf([-2,-5,0]), [0,0,10])

if __name__ == "__main__":

    unittest.main()
