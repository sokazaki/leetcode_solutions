# O(N) Solution with Hash Table

import unittest

def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

class Test(unittest.TestCase):

    def test_containsDuplicate(self):
        self.assertEqual(containsDuplicate([1,2,3,1]), True)
        self.assertEqual(containsDuplicate([1,2,3,4]), False)
        self.assertEqual(containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
        self.assertEqual(containsDuplicate([1]), False)
        self.assertEqual(containsDuplicate([]), False)

if __name__ == "__main__":

    unittest.main()
