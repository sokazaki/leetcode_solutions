# O(NlogN) Solution with Heap

import unittest
import heapq
import collections

def topKFrequent(nums, k):

    if not nums:
        return []
    res = []
    count = collections.Counter(nums)
    vlist = []
    heapq.heapify(vlist)

    for key, val in count.items():
        heapq.heappush(vlist, (-val, key))

    while k:
        top = heapq.heappop(vlist)
        res.append(top[1])
        k -= 1

    return res

class Test(unittest.TestCase):

    def test_topKFrequent(self):
        self.assertCountEqual(topKFrequent([1,1,1,2,2,3], 2), [1,2])
        self.assertCountEqual(topKFrequent([1,1,2,2,3,3,4,4,4,5,5,5], 2), [4,5])
        self.assertCountEqual(topKFrequent([1], 1), [1])
        self.assertCountEqual(topKFrequent([1], 0), [])

if __name__ == "__main__":

    unittest.main()
