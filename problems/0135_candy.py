# O(N) Solution with Greedy Approach

import unittest

def candy(ratings):

    res = len(ratings) * [1]
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            res[i] = res[i-1]+1
    for i in range(len(ratings)-1, 0, -1):
        if ratings[i-1] > ratings[i]:
            res[i-1] = max(res[i-1], res[i]+1)

    return sum(res)


class Test(unittest.TestCase):

    def test_candy(self):
        self.assertEqual(candy([1,0,2]), 5)
        self.assertEqual(candy([1,2,2]), 4)
        self.assertEqual(candy([1,3,4,5,2]), 11)
        self.assertEqual(candy([2,5,4,3,1]), 11)


if __name__ == "__main__":

    unittest.main()
