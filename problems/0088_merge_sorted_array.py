# O(N) Solution with Simple Approach

import unittest

def merge(nums1, m, nums2, n):
    idx1, idx2, last = m-1, n-1, m+n-1
    while idx1 >= 0 and idx2 >= 0:
        if nums2[idx2] > nums1[idx1]:
            nums1[last] = nums2[idx2]
            idx2 -= 1
        else:
            nums1[last] = nums1[idx1]
            idx1 -= 1
        last -= 1
    if idx1 < 0:
        nums1[:idx2+1] = nums2[:idx2+1]

    return nums1


class Test(unittest.TestCase):

    def test_merge(self):
        self.assertListEqual(merge([1,2,3,0,0,0],3,[2,5,6],3), [1,2,2,3,5,6])
        self.assertListEqual(merge([1,2,3,0,0,0,0],3,[2,3,5,6],4), [1,2,2,3,3,5,6])
        self.assertListEqual(merge([1,2,3,0,0,0,0,0],3,[2,3,5,6],4), [1,2,2,3,3,5,6,0])
        self.assertListEqual(merge([0],0,[5],1), [5])
        self.assertListEqual(merge([1],1,[],0), [1])

if __name__ == "__main__":

    unittest.main()
