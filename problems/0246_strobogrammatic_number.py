# O(N) Solution with Hash Map

import unittest

def isStrobogrammatic(num):

    if not num:
        return True

    strobo = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
    for i in range(1+len(num)//2):
        if num[i] not in strobo.values():
            return False
        elif num[len(num)-1-i] not in strobo.values():
            return False
        elif num[i] != strobo[num[len(num)-1-i]]:
            return False

    return True


class Test(unittest.TestCase):

    def test_isStrobogrammatic(self):
        self.assertEqual(isStrobogrammatic("69"), True)
        self.assertEqual(isStrobogrammatic("88"), True)
        self.assertEqual(isStrobogrammatic("848"), False)
        self.assertEqual(isStrobogrammatic("0"), True)
        self.assertEqual(isStrobogrammatic("7"), False)
        self.assertEqual(isStrobogrammatic(""), True)

if __name__ == "__main__":

    unittest.main()
