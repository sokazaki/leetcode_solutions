# O(N) Solution with Queue (like BFS Approach)

import unittest
from collections import deque, defaultdict


def killProcess(pid, ppid, kill):
    res = [kill]
    queue = deque()
    queue.append(kill)
    ppid_to_pid = defaultdict(list)
    for i, p in enumerate(ppid):
        ppid_to_pid[p] += [pid[i]]

    while queue:
        key = queue.pop()
        if len(ppid_to_pid[key]) == 0:
            continue
        for pid in ppid_to_pid[key]:
            res.append(pid)
            queue.appendleft(pid)

    return res


class Test(unittest.TestCase):

    def test_killProcess(self):
        self.assertEqual(killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5), [5, 10])
        self.assertEqual(killProcess([1, 3, 10, 5], [3, 0, 5, 3], 3), [3, 1, 5, 10])
        self.assertEqual(killProcess([1, 3, 10, 5], [3, 0, 5, 3], 1), [1])
        self.assertEqual(killProcess([1, 3, 10, 5], [3, 0, 5, 3], 10), [10])

if __name__ == "__main__":

    unittest.main()
