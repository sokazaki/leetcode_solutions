# O(NlogN) Solution with Simple Sort

import unittest
from functools import cmp_to_key


def largestNumber(nums):

    res = ""
    strlist = []
    for i in nums:
        strlist.append(str(i))
    strlist.sort(key = cmp_to_key(lambda x, y: [1, -1][x+y > y+x]))
    for i in strlist:
        res = res + i
    while res[0] == "0" and len(res) > 1:
        res = res[1::]

    return res


class Test(unittest.TestCase):

    def test_largestNumber(self):
        self.assertEqual(largestNumber([10,2]), "210")
        self.assertEqual(largestNumber([3,30,34,5,9]), "9534330")
        self.assertEqual(largestNumber([0,0]), "0")
        self.assertEqual(largestNumber([1,1,12,21,11,112121]), "21121121211111")


if __name__ == "__main__":

    unittest.main()
