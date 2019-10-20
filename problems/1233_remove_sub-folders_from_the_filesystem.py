# O(NlogN) Solution with Sort + Greedy

import unittest


def removeSubfolders(folder):
    folder.sort()
    res = [folder[0]]
    prev, prev_len = folder[0]+"/", len(folder[0])+1
    for path in folder[1:]:
        if path[:prev_len] != prev:
            res.append(path)
            prev, prev_len = path + "/", len(path)+1
    return res


class Test(unittest.TestCase):

    def test_removeSubfolders(self):
        self.assertEqual(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]), ["/a","/c/d","/c/f"])
        self.assertEqual(removeSubfolders(["/a","/a/b/c","/a/b/d"]), ["/a"])
        self.assertEqual(removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]), ["/a/b/c","/a/b/ca","/a/b/d"])
        self.assertEqual(removeSubfolders(["/b","/a/b/c","/a/b/d", "/a"]), ["/a","/b"])
        self.assertEqual(removeSubfolders(["/a"]), ["/a"])

if __name__ == "__main__":

    unittest.main()
