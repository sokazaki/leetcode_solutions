# O(N) Solution with Stack

import unittest

def simplifyPath(path):
    stack = []
    for ch in path.split("/"):
        if ch not in [".", "..", ""]:
            stack.append(ch)
        if ch == ".." and stack:
            stack.pop()
    return "/" + "/".join(stack)


class Test(unittest.TestCase):

    def test_simplifyPath(self):
        self.assertEqual(simplifyPath("/home/"), "/home")
        self.assertEqual(simplifyPath("/../"), "/")
        self.assertEqual(simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(simplifyPath("/a/./b/../../c/"), "/c")
        self.assertEqual(simplifyPath("/a/../../b/../c//.//"), "/c")
        self.assertEqual(simplifyPath("/a//b////c/d//././/.."), "/a/b/c")
        self.assertEqual(simplifyPath("/.hidden"), "/.hidden")

if __name__ == "__main__":

    unittest.main()
