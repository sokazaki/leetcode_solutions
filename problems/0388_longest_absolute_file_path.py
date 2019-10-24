# O(N) Solution with Simple Approach

import unittest

def lengthLongestPath(input):
    tmp = ""
    paths = []
    for ch in input:
        if ch == '\n' or ch == '\t':
            if tmp != "":
                paths.append(tmp)
            paths.append(ch)
            tmp = ""
        else:
            tmp += ch
    if tmp != "":
        paths.append(tmp)

    res, idx = 0, 0
    curpath = []
    for path in paths:
        if path != '\n' and path != '\t':
            while len(curpath) < idx+1:
                curpath.append("")
            while len(curpath) > idx+1:
                curpath.pop()
            curpath[idx] = path
            if '.' in curpath[-1]:
                res = max(len("".join(curpath))+len(curpath)-1, res)
        elif path == "\n":
            idx = 0
        elif path == "\t":
            idx += 1

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
