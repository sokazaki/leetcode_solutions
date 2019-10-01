# O(N^2) Solution with Simple Approach

import unittest

def generate(numRows):
    res = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
    return res


class Test(unittest.TestCase):

    def test_generate(self):
        self.assertEqual(generate(1), [[1]])
        self.assertEqual(generate(2), [[1],[1,1]])
        self.assertEqual(generate(3), [[1],[1,1],[1,2,1]])
        self.assertEqual(generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        self.assertEqual(generate(7), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1]])

if __name__ == "__main__":

    unittest.main()
