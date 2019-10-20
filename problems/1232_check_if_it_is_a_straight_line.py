# O(N) Solution with Geometry

import unittest


def checkStraightLine(coordinates):
    (x1, y1), (x2, y2) = coordinates[:2]
    for x, y in coordinates:
        if (x - x1) * (y1 - y2) != (x1 - x2) * (y - y1):
            return False
    return True


class Test(unittest.TestCase):

    def test_checkStraightLine(self):
        self.assertEqual(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]), True)
        self.assertEqual(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]), False)
        self.assertEqual(checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]), False)
        self.assertEqual(checkStraightLine([[235,4],[413,2]]), True)
        self.assertEqual(checkStraightLine([[-1,1],[-1,-6],[-1,2],[-1,0],[-1,21],[-1,-4]]), True)

if __name__ == "__main__":

    unittest.main()
