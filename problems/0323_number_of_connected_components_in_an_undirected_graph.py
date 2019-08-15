# O(α(N)) Solution with Union-Find

import unittest


def countComponents(n, edges):

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        if rank[rx] > rank[ry]:
            parent[ry] = rx
        elif rank[rx] < rank[ry]:
            parent[rx] = ry
        else:
            parent[rx] = ry
            rank[ry] += 1

    for x, y in edges:
        union(x, y)

    return len({find(i) for i in range(n)})


class Test(unittest.TestCase):

    def test_countComponents(self):
        self.assertEqual(countComponents(5, [[0,1],[1,2],[3,4]]), 2)
        self.assertEqual(countComponents(5, [[0,1],[1,2],[2,3], [3,4]]), 1)
        self.assertEqual(countComponents(5, []), 5)
        self.assertEqual(countComponents(5, [[0,1],[1,2],[2,3], [3,4],[4,0]]), 1)
        self.assertEqual(countComponents(1, []), 1)
        self.assertEqual(countComponents(0, []), 0)

if __name__ == "__main__":

    unittest.main()
