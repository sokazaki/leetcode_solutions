# O(N) Solution with Hash Table

import unittest
from collections import defaultdict

def findDuplicate(paths):
    dic = defaultdict(list)
    for path in paths:
        path = path.split()
        for i in range(1, len(path)):
            key = path[i].split("(")[1][:-1]
            val = path[0] + "/" + path[i].split("(")[0]
            dic[key].append(val)

    res = []
    for files in dic.values():
        if len(files) >= 2:
            res.append(files)

    return res


class Test(unittest.TestCase):

    def test_findDuplicate(self):
        self.assertCountEqual(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]), [["root/a/1.txt","root/c/3.txt"],["root/a/2.txt","root/c/d/4.txt","root/4.txt"]])
        self.assertCountEqual(findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh) 5.txt(abcd)"]), [["root/a/1.txt","root/c/d/5.txt"]])
        self.assertCountEqual(findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]), [])

if __name__ == "__main__":

    unittest.main()
