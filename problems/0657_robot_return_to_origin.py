# O(N) Solution with Hash Table

import unittest

def judgeCircle(moves):

    lenr = lenl = lenu = lend = 0
    for ch in moves:
        if ch=="R": lenr +=1
        if ch=="L": lenl +=1
        if ch=="U": lenu +=1
        if ch=="D": lend +=1

    return lenr == lenl and lenu == lend

class Test(unittest.TestCase):

    def test_judgeCircle(self):
        self.assertEqual(judgeCircle("UD"), True)
        self.assertEqual(judgeCircle("LL"), False)
        self.assertEqual(judgeCircle("LLRR"), True)
        self.assertEqual(judgeCircle("LLRD"), False)

if __name__ == "__main__":

    unittest.main()
