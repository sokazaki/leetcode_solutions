# O(KlogK) Solution with Heap

import unittest
import heapq


def kSmallestPairs(nums1, nums2, k):

    if not nums1 or not nums2:
        return []

    heap = []

    for i in range(min(len(nums1),k)):
        heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))

    res = []
    while heap and k > 0:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if j+1 <= len(nums2)-1:
            heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        k -= 1

    return res


class Test(unittest.TestCase):

    def test_kSmallestPairs(self):
        self.assertEqual(kSmallestPairs([1,7,11], [2,4,6], 3), [[1,2],[1,4],[1,6]])
        self.assertEqual(kSmallestPairs([1,1,2], [1,2,3], 2), [[1,1],[1,1]])
        self.assertEqual(kSmallestPairs([1,2], [3], 4), [[1,3],[2,3]])
        self.assertEqual(kSmallestPairs([1,2], [3], 2), [[1,3],[2,3]])
        self.assertEqual(kSmallestPairs([1], [-21], 1), [[1,-21]])
        self.assertEqual(kSmallestPairs([1], [], 1), [])
        self.assertEqual(kSmallestPairs([], [], 1), [])

if __name__ == "__main__":

    unittest.main()
