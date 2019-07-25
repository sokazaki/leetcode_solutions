import unittest

def isHappy(n):
    seen = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in seen:
            return False
        else:
            seen.add(n)
    else:
        return True

class Test(unittest.TestCase):

    def test_isHappy(self):
        self.assertEqual(isHappy(19), True)
        self.assertEqual(isHappy(70), True)
        self.assertEqual(isHappy(110), False)
        self.assertEqual(isHappy(193), True)
        self.assertEqual(isHappy(194), False)

if __name__ == "__main__":

    unittest.main()
