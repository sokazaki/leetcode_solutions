# O(N) In-Place Solution with Two Pointers

import unittest

def removeDuplicates(nums):
    tail = 0
    for cur in range(1,len(nums)):
        if nums[cur] != nums[tail]:
            tail += 1
            nums[tail] = nums[cur]
    return nums[:tail+1]


class Test(unittest.TestCase):

    def test_removeDuplicates(self):
        self.assertEqual(removeDuplicates([1,1,2]), [1,2])
        self.assertEqual(removeDuplicates([0,0,1,1,1,2,2,3,3,4]), [0,1,2,3,4])
        self.assertEqual(removeDuplicates([1]), [1])
        self.assertEqual(removeDuplicates([1,1,1,1]), [1])
        self.assertEqual(removeDuplicates([-10,-10,1,1,1,22,22,33,333,444]), [-10,1,22,33,333,444])

if __name__ == "__main__":

    unittest.main()
