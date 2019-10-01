# O(N) Solution with Simple Approach

import unittest

def plusOne(digits):
    digits[-1] += 1
    for i in range(len(digits)-1, 0, -1):
        if digits[i] != 10:
            break
        digits[i] = 0
        digits[i-1] += 1

    if digits[0] == 10:
        digits[0] = 0
        return [1] + digits
    return digits


class Test(unittest.TestCase):

    def test_plusOne(self):
        self.assertEqual(plusOne([1,2,3]), [1,2,4])
        self.assertEqual(plusOne([1,2,9]), [1,3,0])
        self.assertEqual(plusOne([9,9,9]), [1,0,0,0])
        self.assertEqual(plusOne([0]), [1])
        self.assertEqual(plusOne([9,0,9]), [9,1,0])

if __name__ == "__main__":

    unittest.main()
