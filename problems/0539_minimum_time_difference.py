# O(N) Solution with Simple Approach

import unittest

def findMinDifference(timePoints):

    t = sorted(int(t[:2])*60+int(t[3:]) for t in timePoints)
    t.append(t[0]+24*60)

    return min(b-a for a, b in zip(t, t[1:]))


class Test(unittest.TestCase):

    def test_findMinDifference(self):
        self.assertEqual(findMinDifference(["23:59","00:00"]), 1)
        self.assertEqual(findMinDifference(["23:59","00:05", "00:02"]), 3)
        self.assertEqual(findMinDifference(["23:50","14:10","23:59","10:00","00:45"]), 9)
        self.assertEqual(findMinDifference(["23:50","14:10","23:59","10:00","00:03","00:45"]), 4)
        self.assertEqual(findMinDifference(["23:50","14:10","23:59","10:00","00:03","00:45","14:11"]), 1)

if __name__ == "__main__":

    unittest.main()
