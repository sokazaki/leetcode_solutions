# O(NlogN) Solution with Sort + Greedy

import unittest


def removeSubfolders(folder):
    folder.sort()
    diff = folder[0]
    res = [folder[0]]
    for path in folder[1:]:
        if diff + "/" in path:
            continue
        else:
            diff = path
            res.append(path)

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
