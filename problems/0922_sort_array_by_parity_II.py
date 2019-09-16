# O(N) Solution with Simple Approach

import unittest

def sortArrayByParityII(A):
    i = 0
    j = 1

    while i < len(A) and j < len(A):
        if A[i] % 2 == 0:
            i += 2
        elif A[j] % 2 == 1:
            j += 2
        else:
            A[i], A[j] = A[j], A[i]
            i += 2
            j += 2

    return A


class Test(unittest.TestCase):

    def test_sortArrayByParityII(self):
        self.assertEqual(sortArrayByParityII([4,2,5,7]), [4,5,2,7])
        self.assertEqual(sortArrayByParityII([4,2,7,5]), [4,7,2,5])
        self.assertEqual(sortArrayByParityII([4,4,4,1,1,1]), [4,1,4,1,4,1])
        self.assertEqual(sortArrayByParityII([1,1,1,4,4,4]), [4,1,4,1,4,1])
        self.assertEqual(sortArrayByParityII([]), [])

if __name__ == "__main__":

    unittest.main()
