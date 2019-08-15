 O(N) Solution with Dynamic Programming

import unittest

def rob(nums):

    def simple_rob(nums):
        r, nr = 0, 0
        for n in nums:
            r, nr = nr + n, max(r, nr)
        return max(r, nr)

    if len(nums) == 1:
        return nums[0]
    else:
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

class Test(unittest.TestCase):

    def test_rob(self):
        self.assertEqual(rob([1,2,3,1]), 4)
        self.assertEqual(rob([2,1,1,2]), 3)
        self.assertEqual(rob([2,7,9,3,1]), 11)
        self.assertEqual(rob([1,5,1,1,7,8]), 14)
        self.assertEqual(rob([8]), 8)

if __name__ == "__main__":

    unittest.main()
