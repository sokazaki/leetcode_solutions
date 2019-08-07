# O(k+(N-k)logk) Solution with Heap

import unittest
import heapq

def findKthLargest(nums, k):

    minheap = nums[:k]
    heapq.heapify(minheap) # O(k)
    for num in nums[k:]: # O(n-k)
        if num > minheap[0]:
            heapq.heapreplace(minheap, num) # O(logk)

    return minheap[0]


class Test(unittest.TestCase):

    def test_findKthLargest(self):
        self.assertEqual(findKthLargest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)
        self.assertEqual(findKthLargest([9], 1), 9)
        self.assertEqual(findKthLargest([-3,2,-3,-1,0,4,5,-1,6], 3), 4)


if __name__ == "__main__":

    unittest.main()
