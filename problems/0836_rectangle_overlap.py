# O(1) Solution with Simple Math

import unittest

def isRectangleOverlap(rec1, rec2):
    dx = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
    dy = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
    if (dx>0) and (dy>0):
        return True
    else:
        return False


class Test(unittest.TestCase):

    def test_isRectangleOverlap(self):
        self.assertEqual(isRectangleOverlap([0,0,2,2], [1,1,3,3]), True)
        self.assertEqual(isRectangleOverlap([0,0,1,1], [1,0,2,1]), False)
        self.assertEqual(isRectangleOverlap([0,0,1,1], [1,1,3,3]), False)
        self.assertEqual(isRectangleOverlap([0,0,2,2], [-1,-1,3,3]), True)
        self.assertEqual(isRectangleOverlap([0,0,2,2], [-1,-1,1,1]), True)

if __name__ == "__main__":

    unittest.main()
