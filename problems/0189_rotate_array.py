# O(N) Time Complexity / O(1) Space Complexity Solution with Simple Approach

import unittest

class Solution:
    def rotate(self, nums, k):

        k, n = k%len(nums), len(nums)-1

        self.reverse(nums, 0, n-k)
        self.reverse(nums, n-k+1, n)
        self.reverse(nums, 0, n)

        return nums

    def reverse(self, nums, i, j):

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1


class Test(unittest.TestCase):

    def test_rotate(self):
        ans = Solution()
        self.assertEqual(ans.rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
        self.assertEqual(ans.rotate([1,2,3,4,5,6,7], 0), [1,2,3,4,5,6,7])
        self.assertEqual(ans.rotate([1,2,3,4,5,6,7], 13), [2,3,4,5,6,7,1])
        self.assertEqual(ans.rotate([1,2,3,4,5,6,7], 1), [7,1,2,3,4,5,6])
        self.assertEqual(ans.rotate([-1,-100,3,99], 2), [3,99,-1,-100])


if __name__ == "__main__":

    unittest.main()
