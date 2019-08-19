# O(N) Solution with Simple Solution

import unittest

def singleNumber(nums):

    res = 0
    for num in nums:
        res ^= num

    return res


class Test(unittest.TestCase):

    def test_singleNumbere(self):
        self.assertEqual(singleNumber([2,2,1]), 1)
        self.assertEqual(singleNumber([1]), 1)
        self.assertEqual(singleNumber([4,1,2,1,2]), 4)
        self.assertEqual(singleNumber([2, 2**30, 2**30]), 2)
        self.assertEqual(singleNumber([2**30-1, 2**30, 2**30-1]), 2**30)

if __name__ == "__main__":

    unittest.main()
