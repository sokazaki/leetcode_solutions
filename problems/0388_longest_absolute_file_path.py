# O(N) Solution with Simple Approach

import unittest
from collections import defaultdict

def lengthLongestPath(input):
    input = input.split("\n")
    dic = defaultdict(str)
    res = 0

    for i in input:
        candidate = i.split("\t")
        idx = candidate.count("")
        dic[idx] = i.split("\t")[-1]
        path = []
        if "." in dic[idx]:
            for i in range(idx+1):
                path.append(dic[i])
            res = max(res, len("/".join(path)))

    return res


class Test(unittest.TestCase):

    def test_lengthLongestPath(self):
        self.assertEqual(lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"), 20)
        self.assertEqual(lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"), 32)
        self.assertEqual(lengthLongestPath("a"), 0)
        self.assertEqual(lengthLongestPath("a.txt"), 5)
        self.assertEqual(lengthLongestPath("dir\n file.txt"), 9)

if __name__ == "__main__":

    unittest.main()
