# O(N) Solution with Hash Map

import unittest

def containsNearbyDuplicate(nums, k):

    dic = {}
    for i, num in enumerate(nums):
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i

    return False


class Test(unittest.TestCase):

    def test_containsNearbyDuplicate(self):
        self.assertEqual(containsNearbyDuplicate([1,2,3,1], 3), True)
        self.assertEqual(containsNearbyDuplicate([1,0,1,1], 1), True)
        self.assertEqual(containsNearbyDuplicate([1,2,3,1,2,3], 2), False)
        self.assertEqual(containsNearbyDuplicate([1,2,3,1,2,2], 1), True)
        self.assertEqual(containsNearbyDuplicate([1], 1), False)
        self.assertEqual(containsNearbyDuplicate([], 1), False)

if __name__ == "__main__":

    unittest.main()
