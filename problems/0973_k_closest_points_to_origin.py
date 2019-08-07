# O(NlogK) Solution with Heap

import unittest
import heapq

def kClosest(points, K):

    return heapq.nsmallest(K, points, lambda x: x[0]**2+x[1]**2)


class Test(unittest.TestCase):

    def test_kClosest(self):
        self.assertCountEqual(kClosest([[1,3],[-2,2]], 1), [[-2,2]])
        self.assertCountEqual(kClosest([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]])
        self.assertCountEqual(kClosest([[2,2]], 3), [[2,2]])
        self.assertCountEqual(kClosest([[2,2]], 0), [])

if __name__ == "__main__":

    unittest.main()
