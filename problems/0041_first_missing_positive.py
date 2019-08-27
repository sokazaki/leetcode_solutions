# O(N) Time Complexity / O(1) Space Complexity Solution with Hashmap

import unittest

def firstMissingPositive(nums):

    if 1 not in nums:
        return 1
    if len(nums) == 1:
        return 2

    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums):
            nums[i] = 1

    for i in range(len(nums)):
        num = abs(nums[i])
        nums[num-1] = -abs(nums[num-1])

    for i in range(len(nums)):
        if nums[i] > 0:
            return i+1

    return len(nums)+1


class Test(unittest.TestCase):

    def test_firstMissingPositive(self):
        self.assertEqual(firstMissingPositive([1,2,0]), 3)
        self.assertEqual(firstMissingPositive([3,4,-1,1]), 2)
        self.assertEqual(firstMissingPositive([7,8,9,11,12]), 1)
        self.assertEqual(firstMissingPositive([2,2]), 1)
        self.assertEqual(firstMissingPositive([]), 1)


if __name__ == "__main__":

    unittest.main()
