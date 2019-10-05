# O(N) Solution with Simple Approach

import unittest
from collections import Counter

def leastInterval(tasks, n):

    count = Counter(tasks)
    most = count.most_common()[0][1]
    num_most = len([char for char, freq in count.items() if freq == most])
    time = (most - 1) * (n + 1) + num_most
    return max(time, len(tasks))


class Test(unittest.TestCase):

    def test_leastInterval(self):
        self.assertEqual(leastInterval(["A","A","A","B","B","B"], 2), 8)
        self.assertEqual(leastInterval(["A","B","A","B","A","B"], 2), 8)
        self.assertEqual(leastInterval(["A","A","C","B","B","C"], 3), 7)
        self.assertEqual(leastInterval(["A","C","A","D","B","E"], 4), 6)
        self.assertEqual(leastInterval(["A","A","A","B","B","B", "F", "E", "D"], 2), 9)

if __name__ == "__main__":

    unittest.main()
