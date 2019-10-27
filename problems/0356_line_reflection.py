# O(N) Solution with Hashmap

import unittest

def isReflected(points):

    if not points:
        return True
    points = set([(x, y) for x, y in points])
    mid = (min(x for x, _ in points) + max(x for x, _ in points)) / 2

    for x, y in points:
        reflect_x = mid + (mid-x)
        if (reflect_x, y) not in points:
            return False

    return True


class Test(unittest.TestCase):

    def test_isReflected(self):
        self.assertEqual(isReflected([[1,1],[-1,1]]), True)
        self.assertEqual(isReflected([[1,1],[-1,-1]]), False)
        self.assertEqual(isReflected([[0,0],[0,-1]]), True)
        self.assertEqual(isReflected([[-16,1],[16,1],[16,1]]), True)
        self.assertEqual(isReflected([[1,1],[0,1],[-1,1],[0,0]]), True)
        self.assertEqual(isReflected([[2,0],[2,1],[2,2],[2,3],[2,4],[-2,0],[-2,1],[-2,2],[-2,3],[-2,4]]), True)


if __name__ == "__main__":

    unittest.main()
