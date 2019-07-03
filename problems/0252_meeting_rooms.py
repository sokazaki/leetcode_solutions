# O(NlogN) Solution with Sort

import unittest

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True


class Test(unittest.TestCase):

    def test_canAttendMeetingsself):
        self.assertEqual(canAttendMeetings([[0,30],[50,60],[15,20]]), False)
        self.assertEqual(canAttendMeetings([[0,30],[5,10],[15,20]]), False)
        self.assertEqual(canAttendMeetings([[7,10],[2,4]]), True)
        self.assertEqual(canAttendMeetings([[7,10]]), True)
        self.assertEqual(canAttendMeetings([]), True)


if __name__ == "__main__":

    unittest.main()
