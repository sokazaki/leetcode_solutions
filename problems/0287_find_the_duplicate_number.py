# O(N) Time Complexity / O(1) Space Complexity Solution with Two Pointers

import unittest

def findDuplicate(nums):
    slow = fast = res = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            while res != slow:
                res = nums[res]
                slow = nums[slow]
            return res


class Test(unittest.TestCase):

    def test_findDuplicate(self):
        self.assertEqual(findDuplicate([1,3,4,2,2]), 2)
        self.assertEqual(findDuplicate([3,1,3,4,2]), 3)
        self.assertEqual(findDuplicate([2,2,2,2,2]), 2)
        self.assertEqual(findDuplicate([1,2,3,4,5,6,7,7,8]), 7)


if __name__ == "__main__":

    unittest.main()
