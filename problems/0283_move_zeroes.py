# O(N) Solution with Two Pointers

import unittest


def moveZeroes(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums


class Test(unittest.TestCase):

    def test_moveZeroes(self):
        self.assertListEqual(moveZeroes([0,1,0,3,12]), [1,3,12,0,0])
        self.assertListEqual(moveZeroes([1,0,0,2]), [1,2,0,0])
        self.assertListEqual(moveZeroes([0,0,0,1,0,1,0,1,0]), [1,1,1,0,0,0,0,0,0])
        self.assertListEqual(moveZeroes([1]), [1])
        self.assertListEqual(moveZeroes([]), [])

if __name__ == "__main__":

    unittest.main()
