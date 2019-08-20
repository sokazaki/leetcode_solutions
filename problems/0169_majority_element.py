# O(N) Solution with HashMap

import unittest


def majorityElement(nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums)//2:
            return num
        else:
            dic[num] += 1


class Test(unittest.TestCase):

    def test_majorityElement(self):
        self.assertEqual(majorityElement([3,2,3]), 3)
        self.assertEqual(majorityElement([2,2,1,1,1,2,2]), 2)
        self.assertEqual(majorityElement([0,0,0,1,1,0,1,0]), 0)
        self.assertEqual(majorityElement([1,1,1,1,1,2,6,6]), 1)
        self.assertEqual(majorityElement([0,0,0]), 0)

if __name__ == "__main__":

    unittest.main()
