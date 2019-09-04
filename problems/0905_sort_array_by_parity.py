# O(N) In-Place Solution with Two Pointers

import unittest

def sortArrayByParity(A):

    i, j = 0, len(A)-1

    while i < j:
        m, n = A[i], A[j]
        if m%2==1 and n%2==0:
            A[i], A[j] = n, m
        elif m%2==1:
            j -= 1
        elif n%2==0:
            i += 1
        else:
            i += 1
            j -= 1

    return A


class Test(unittest.TestCase):

    def test_sortArrayByParity(self):
        self.assertEqual(sortArrayByParity([3,1,2,4]), [4,2,1,3])
        self.assertEqual(sortArrayByParity([1]), [1])
        self.assertEqual(sortArrayByParity([]), [])
        self.assertEqual(sortArrayByParity([1,2,1,2,1,1]), [2,2,1,1,1,1])
        self.assertEqual(sortArrayByParity([1,2,2,2,2,2]), [2,2,2,2,2,1])


if __name__ == "__main__":

    unittest.main()
