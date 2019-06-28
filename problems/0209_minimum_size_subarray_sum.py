# O(N) Solution with Two Pointers and Sliding Window
# (Another: O(NlogN) Solution with Cumulative Sum + Binary Search)
# (Another: O(N^2) Solution with Simple Brute-force approach)

import unittest

def minSubArrayLen(s, nums):

    min_length = len(nums) + 1
    start = count = 0
    for i, c in enumerate(nums):
        count += c
        while count >= s:
            min_length = min(min_length, i - start + 1)
            count -= nums[start]
            start += 1

    return min_length if min_length <= len(nums) else 0

class Test(unittest.TestCase):

    def test_minSubArrayLen(self):
        self.assertEqual(minSubArrayLen(7, [2,3,1,2,4,3]), 2)
        self.assertEqual(minSubArrayLen(10, [2,3,1,2,4,3]), 4)
        self.assertEqual(minSubArrayLen(11, [2,3,1,2,4,3]), 5)
        self.assertEqual(minSubArrayLen(100, [2,3,1,2,4,3]), 0)
        self.assertEqual(minSubArrayLen(9, [11]), 1)
        self.assertEqual(minSubArrayLen(11, [9]), 0)
        self.assertEqual(minSubArrayLen(9, []), 0)


if __name__ == "__main__":

    unittest.main()
