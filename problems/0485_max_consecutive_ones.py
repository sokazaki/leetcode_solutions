# O(N) Solution with Simple Solution

import unittest

def findMaxConsecutiveOnes(nums):

    res = 0
    tmp = 0
    for num in nums:
        if num==1:
            tmp += 1
            res = max(res, tmp)
        else:
            tmp=0

    return res


class Test(unittest.TestCase):

    def test_findMaxConsecutiveOnes(self):
        self.assertEqual(findMaxConsecutiveOnes([1,0,1,1,0,1]), 2)
        self.assertEqual(findMaxConsecutiveOnes([1,1,0,1,1,1]), 3)
        self.assertEqual(findMaxConsecutiveOnes([1]), 1)
        self.assertEqual(findMaxConsecutiveOnes([1,1,1]), 3)
        self.assertEqual(findMaxConsecutiveOnes([0,0,1,1,1]), 3)
        self.assertEqual(findMaxConsecutiveOnes([0,0,1,1,1,1,0]), 4)


if __name__ == "__main__":

    unittest.main()
