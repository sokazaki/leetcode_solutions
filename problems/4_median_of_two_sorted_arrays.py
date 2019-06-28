# O(log(min(N,M)) Solution with Binary Search
# (Another: O((N＋M)log(N+M)) Solution with Simple approach)

import unittest

def findMedianSortedArrays(nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    med_idx = int((m+n-1)/2)
    lo, hi = 0, m
    while lo < hi:
        i = int((lo+hi)/2)
        if med_idx-i-1 < 0 or a[i] >= b[med_idx-i-1]:
            hi = i
        else:
            lo = i + 1
    i = lo
    med = sorted(a[i:i+2] + b[med_idx-i:med_idx-i+2])
    return (med[0] + med[1-(m+n)%2]) / 2.0


class Test(unittest.TestCase):

    def test_findMedianSortedArrays(self):
        self.assertEqual(findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(findMedianSortedArrays([2], [1, 3]), 2.0)
        self.assertEqual(findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(findMedianSortedArrays([2,3,4,5,6], [3,4]), 4.0)
        self.assertEqual(findMedianSortedArrays([-2,-3,4,5,6], [3,4]), 4.0)
        self.assertEqual(findMedianSortedArrays([-2,0,4,5,6], [3,4]), 4.0)


if __name__ == "__main__":

    unittest.main()
