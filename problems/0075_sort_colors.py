# O(N) Solution with One-Pass Approach

import unittest

def sortColors(nums):

    red, white, blue = 0, 0, len(nums)-1

    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1


    return nums


class Test(unittest.TestCase):

    def test_sortColors(self):
        self.assertEqual(sortColors([2,1,1,0,1,2,0,1]), [0,0,1,1,1,1,2,2])
        self.assertEqual(sortColors([2,2,1,1,1,1,0,0]), [0,0,1,1,1,1,2,2])
        self.assertEqual(sortColors([0,0,1,1,1,1,2,2]), [0,0,1,1,1,1,2,2])
        self.assertEqual(sortColors([2]), [2])
        self.assertEqual(sortColors([]), [])


if __name__ == "__main__":

    unittest.main()
