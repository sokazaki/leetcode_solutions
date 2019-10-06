# O(N) Solution with Hash Table

import unittest


def findWords(words):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    res = []
    for word in words:
        w = set(word.lower())
        if w <= line1 or w <= line2 or w <= line3:
            res.append(word)
    return res


class Test(unittest.TestCase):

    def test_findWords(self):
        self.assertCountEqual(findWords(["Hello","Alaska","Dad","Peace"]), ["Alaska", "Dad"])
        self.assertCountEqual(findWords(["Hello","Aleksa","Dad","Peace"]), ["Dad"])
        self.assertCountEqual(findWords(["Hello","Alaska","DDD","Dad","PeACe"]), ["Alaska", "Dad", "DDD"])
        self.assertCountEqual(findWords(["A","C","A","D","B","E"]), ["A","C","A","D","B","E"])
        self.assertCountEqual(findWords([""]), [""])

if __name__ == "__main__":

    unittest.main()
