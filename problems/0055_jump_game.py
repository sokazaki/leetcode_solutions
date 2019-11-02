# O(N) Solution with Greedy Approach

import unittest

def canJump(nums):
    curmax = 0
    for idx, num in enumerate(nums):
        if idx > curmax:
            return False
        curmax = max(curmax, idx+num)
    return True

class Test(unittest.TestCase):

    def test_canJump(self):
        self.assertEqual(canJump([2,3,1,1,4]), True)
        self.assertEqual(canJump([3,2,1,0,4]), False)
        self.assertEqual(canJump([0]), True)
        self.assertEqual(canJump([0,4]), False)
        self.assertEqual(canJump([3,0,0,0,4]), False)


if __name__ == "__main__":

    unittest.main()
