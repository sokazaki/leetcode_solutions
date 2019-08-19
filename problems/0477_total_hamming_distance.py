# O(N) Solution with Simple Solution

import unittest

def totalHammingDistance(nums):

    res = 0
    mask = 1
    for _ in range(0, 32):
        ones = zeros = 0
        for num in nums:
            if num & mask:
                ones += 1
            else:
                zeros += 1
        res += ones * zeros
        mask = mask << 1

    return res


class Test(unittest.TestCase):

    def test_totalHammingDistance(self):
        self.assertEqual(totalHammingDistance([4, 14, 2]), 6)
        self.assertEqual(totalHammingDistance([1]), 0)
        self.assertEqual(totalHammingDistance([1,1,2,1,1,1]), 10)
        self.assertEqual(totalHammingDistance([2, 2**30]), 2)
        self.assertEqual(totalHammingDistance([2**30-1, 2**30]), 31)

if __name__ == "__main__":

    unittest.main()
