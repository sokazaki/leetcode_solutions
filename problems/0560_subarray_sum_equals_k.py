# O(N) Solution with Hash Map

import unittest


def subarraySum(nums, k):

    cumsum, cur, res = {0: 1}, 0, 0

    for val in nums:
        cur += val
        res += cumsum.get(cur-k, 0)
        cumsum[cur] = cumsum.get(cur, 0) + 1

    return res


class Test(unittest.TestCase):

    def test_subarraySum(self):
        self.assertEqual(subarraySum([1,1,1], 2), 2)
        self.assertEqual(subarraySum([1,5,6], 3), 0)
        self.assertEqual(subarraySum([1], 1), 1)
        self.assertEqual(subarraySum([], 1), 0)
        self.assertEqual(subarraySum([-1, 1, 0, 0, -1], 0), 7)
        self.assertEqual(subarraySum([-1, 0, 0, 0, 1], 0), 7)

if __name__ == "__main__":

    unittest.main()
