# O(N) Solution with Two Pointers

import unittest

def maxArea(height):
    res = 0
    l, r = 0, len(height)-1

    while l < r:
        if height[l] < height[r]:
            area = height[l]*(r-l)
            l += 1
        else:
            area = height[r]*(r-l)
            r -= 1
        res = max(res, area)

    return res


class Test(unittest.TestCase):

    def test_maxArea(self):
        self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(maxArea([4,8,6,2,5,4,8,3,2]), 40)
        self.assertEqual(maxArea([4,0,6,2,5,4,0,3,2]), 21)
        self.assertEqual(maxArea([4,4]), 4)


if __name__ == "__main__":

    unittest.main()
