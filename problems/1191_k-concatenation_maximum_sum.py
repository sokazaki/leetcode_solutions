# O(N) Solution with Kadane's Algorithm

import unittest

def kConcatenationMaxSum(arr, k):

    def Kadane(arr):
        res = cur = 0
        for num in arr:
            cur = max(num, num + cur)
            res = max(res, cur)
        return res

    if k > 1:
        return ((k-2) * max(sum(arr), 0) + Kadane(arr*2)) % (10**9+7)
    else:
        return Kadane(arr) % (10**9+7)


class Test(unittest.TestCase):

    def test_kConcatenationMaxSum(self):
        self.assertEqual(kConcatenationMaxSum([1,2], 3), 9)
        self.assertEqual(kConcatenationMaxSum([1,-2,1], 5), 2)
        self.assertEqual(kConcatenationMaxSum([-1,-2], 7), 0)
        self.assertEqual(kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4], 5), 20)
        self.assertEqual(kConcatenationMaxSum([1], 1), 1)

if __name__ == "__main__":

    unittest.main()
