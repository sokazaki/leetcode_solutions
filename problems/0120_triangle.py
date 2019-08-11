# In-Place Solution with Dynamic Programming

import unittest

def minimumTotal(triangle):

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])

    return min(triangle[-1])

[[2],[3,4],[6,5,7],[4,1,8,3]]

class Test(unittest.TestCase):

    def test_minimumTotal(self):
        self.assertEqual(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]), 11)
        self.assertEqual(minimumTotal([[2],[3,4],[6,5,7],[-1,1,8,3]]), 10)
        self.assertEqual(minimumTotal([[2],[13,-4],[-6,5,7],[-1,1,-8,3]]), -5)
        self.assertEqual(minimumTotal([[1]]), 1)

if __name__ == "__main__":

    unittest.main()
