# Time: O(N)/Space: O(1) Solution with Inverting Sign

import unittest

def findDisappearedNumbers(nums):

    for i in range(len(nums)):
        idx = abs(nums[i]) - 1
        nums[idx] = - abs(nums[idx])

    return [i+1 for i in range(len(nums)) if nums[i] > 0]

class Test(unittest.TestCase):

    def test_findDisappearedNumbers(self):
        self.assertListEqual(findDisappearedNumbers([4,3,2,7,8,2,3,1]), [5,6])
        self.assertListEqual(findDisappearedNumbers([4,3,5,7,8,2,3,1]), [6])
        self.assertListEqual(findDisappearedNumbers([4,3,5,7,8,2,3,1,1]), [6,9])
        self.assertListEqual(findDisappearedNumbers([1,2]), [])

if __name__ == "__main__":

    unittest.main()
