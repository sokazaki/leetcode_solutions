# O(N^2) Solution with Sort and Two Pointers

import unittest


def threeSumSmaller(nums, target):
    nums.sort()
    res = 0
    for i in range(len(nums)):
        if sum(nums[i:i+3]) >= target:
            break
        j, k = i+1, len(nums)-1
        while j < k:
            if nums[i]+nums[j]+nums[k] < target:
                res += k-j
                j += 1
            else:
                k -= 1
    return res


class Test(unittest.TestCase):

    def test_threeSumSmaller(self):
        self.assertEqual(threeSumSmaller([3,2,-2,6,2,-2,6,-2,-4,2,3,0,4,4,1], 3), 151)
        self.assertEqual(threeSumSmaller([-2,0,1,3], 2), 2)
        self.assertEqual(threeSumSmaller([0], 0), 0)
        self.assertEqual(threeSumSmaller([-1,2,1], 100), 1)
        self.assertEqual(threeSumSmaller([-1,2,1,-4], 1), 3)

if __name__ == "__main__":

    unittest.main()
