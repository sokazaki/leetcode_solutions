# O(N+M) Solution with Two Pointers

import unittest


def intervalIntersection(A, B):

    i, j, res = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i][1] < B[j][0]:
            i += 1
        elif B[j][1] < A[i][0]:
            j += 1
        else:
            res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

    return res


class Test(unittest.TestCase):

    def test_intervalIntersection(self):
        self.assertEqual(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
        self.assertEqual(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[26,27]]), [[1,2],[5,5],[8,10],[15,23],[24,24]])
        self.assertEqual(intervalIntersection([[0,2]], [[8,12]]), [])
        self.assertEqual(intervalIntersection([[0,2],[5,10],[25,26]], [[3,4],[15,24],[27,28]]), [])

if __name__ == "__main__":

    unittest.main()
