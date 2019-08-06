# O(N^2) Solution with Greedy Sort & Insert Approach

import unittest

def reconstructQueue(people):
    people = sorted(people, key=lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        res.insert(p[1], p)

    return res


class Test(unittest.TestCase):

    def test_reconstructQueue(self):
        self.assertListEqual(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]), [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]])
        self.assertListEqual(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2],[4,5],[0,0]]), [[0,0],[5,0],[7,0],[5,2],[6,1],[4,4],[4,5],[7,1]])
        self.assertListEqual(reconstructQueue([[6,0],[5,1],[4,2],[3,3],[2,4],[1,1]]), [[6,0],[1,1],[5,1],[4,2],[3,3],[2,4]])
        self.assertListEqual(reconstructQueue([[6,0],[5,1],[4,2],[3,3],[2,4],[1,5]]), [[6,0],[5,1],[4,2],[3,3],[2,4],[1,5]])


if __name__ == "__main__":

    unittest.main()
