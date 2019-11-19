# O(N) Solution with Greedy

import unittest


def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    cum, res = 0, -1
    for idx, (i, j) in enumerate(zip(gas, cost)):
        cum += i - j
        if cum < 0:
            cum = 0
            res = -1
            continue
        elif res == -1:
            res = idx

    return res


class Test(unittest.TestCase):

    def test_canCompleteCircuit(self):
        self.assertEqual(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]), 3)
        self.assertEqual(canCompleteCircuit([2,3,4], [3,4,3]), -1)
        self.assertEqual(canCompleteCircuit([2,3,7], [4,5,3]), 2)
        self.assertEqual(canCompleteCircuit([1], [1]), 0)

if __name__ == "__main__":

    unittest.main()
