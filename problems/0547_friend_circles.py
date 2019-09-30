# O(N^2) Solution with DFS

import unittest

def findCircleNum(M):

    visited = set()
    def dfs(node):
        for idx, node in enumerate(M[node]):
            if node and idx not in visited:
                visited.add(idx)
                dfs(idx)

    res = 0
    for i in range(len(M)):
        if i not in visited:
            dfs(i)
            res += 1

    return res


class Test(unittest.TestCase):

    def test_findCircleNum(self):
        self.assertEqual(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]), 2)
        self.assertEqual(findCircleNum([[1,1,0],[1,1,1],[0,1,1]]), 1)
        self.assertEqual(findCircleNum([[1,0,0],[0,1,0],[0,0,1]]), 3)
        self.assertEqual(findCircleNum([[1,1,0,1,1],[1,1,0,1,1],[0,0,1,0,0],[1,1,0,1,1],[1,1,0,1,1]]), 2)
        self.assertEqual(findCircleNum([[1]]), 1)

if __name__ == "__main__":

    unittest.main()
