# O(logN) Solution with Binary Search

import unittest


def shipWithinDays(weights, D):
    def cannot_split(max_weight):
        sum_weight = 0
        days = 1
        for weight in weights:
            sum_weight += weight
            if sum_weight > max_weight:
                sum_weight = weight
                days += 1
        return days > D

    low, high = max(weights), sum(weights)
    while low < high:
        mid = low + (high-low) // 2
        if cannot_split(mid):
            low = mid+1
        else:
            high = mid
    return low


class Test(unittest.TestCase):

    def test_shipWithinDays(self):
        self.assertEqual(shipWithinDays([1,2,3,4,5,6,7,8,9,10],5), 15)
        self.assertEqual(shipWithinDays([3,2,2,4,1,4],3), 6)
        self.assertEqual(shipWithinDays([1,2,3,1,1],4), 3)
        self.assertEqual(shipWithinDays([1,2,3,7,9],5), 9)
        self.assertEqual(shipWithinDays([1,2,3,1,1],1), 8)


if __name__ == "__main__":

    unittest.main()
