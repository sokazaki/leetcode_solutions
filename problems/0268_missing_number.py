# O(N) Solution with Simple Math

import unittest


def missingNumber(nums):

    return len(nums)*(len(nums)+1)/2 - sum(nums)


class Test(unittest.TestCase):

    def test_missingNumber(self):
        self.assertEqual(missingNumber([1,2,3]), 0)
        self.assertEqual(missingNumber([0,1,2,4,5,6,7,8]), 3)
        self.assertEqual(missingNumber([0,1]), 2)
        self.assertEqual(missingNumber([3,5,8,6,7,1,0,2]), 4)
        self.assertEqual(missingNumber([0]), 1)

if __name__ == "__main__":

    unittest.main()
