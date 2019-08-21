# Simple Solution with Built-In Sort

import unittest

def reorderLogFiles(logs):

    digits = []
    letters = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key = lambda x: x.split()[0])
    letters.sort(key = lambda x: x.split()[1:])

    return letters + digits


class Test(unittest.TestCase):

    def test_reorderLogFiles(self):
        self.assertEqual(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]), ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])
        self.assertEqual(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]), ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])
        self.assertEqual(reorderLogFiles([]), [])
        self.assertEqual(reorderLogFiles(["g1 act car","g1 act caa r","g2 act car","g1 act","g0 xyz"]), ["g1 act","g1 act caa r","g1 act car","g2 act car","g0 xyz"])
        self.assertEqual(reorderLogFiles(["a1 9 2 3 1","a1 9 2 5 1","a2 9 2 3 1","a1 9 2 35 1","a1 9"]), ["a1 9 2 3 1","a1 9 2 5 1","a2 9 2 3 1","a1 9 2 35 1","a1 9"])

if __name__ == "__main__":

    unittest.main()
