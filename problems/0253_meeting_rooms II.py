# O(NlogN) Solution with Sort and Heap

import unittest
import heapq

def minMeetingRooms(intervals):
    intervals.sort(key=lambda x:x[0])
    heap = []

    for i in intervals:
        if heap and i[0] >= heap[0]:
            heapq.heapreplace(heap, i[1])
        else:
            heapq.heappush(heap, i[1])

    return len(heap)

class Test(unittest.TestCase):

    def test_minMeetingRooms(self):
        self.assertEqual(minMeetingRooms([[0, 30],[5, 10],[15, 20]]), 2)
        self.assertEqual(minMeetingRooms([[7,10],[2,4]]), 1)
        self.assertEqual(minMeetingRooms([[0, 30],[5, 10],[15, 20], [25, 50]]), 2)
        self.assertEqual(minMeetingRooms([[0, 30],[5, 10],[15, 20], [5, 50]]), 3)
        self.assertEqual(minMeetingRooms([[0, 30]]), 1)
        self.assertEqual(minMeetingRooms([]), 0)


if __name__ == "__main__":

    unittest.main()
