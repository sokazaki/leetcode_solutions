# O(N) Solution with Greedy

import unittest

def checkPossibility(nums):

    count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            count += 1
            if i == 0:
                nums[i] = nums[i+1]
            elif nums[i-1] <= nums[i+1]:
                nums[i] = nums[i-1]
            else:
                nums[i+1] = nums[i]
        if count > 1:
            return False

    return True


class Test(unittest.TestCase):

    def test_checkPossibility(self):
        self.assertEqual(checkPossibility([4,2,3]), True)
        self.assertEqual(checkPossibility([4,2,1]), False)
        self.assertEqual(checkPossibility([1,4,0,3]), False)
        self.assertEqual(checkPossibility([3,4,2,3]), False)
        self.assertEqual(checkPossibility([-1,4,2,3]), True)
        self.assertEqual(checkPossibility([5,2,5,5,5]), True)

if __name__ == "__main__":

    unittest.main()
