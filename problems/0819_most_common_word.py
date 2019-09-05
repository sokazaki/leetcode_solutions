# O(N) Solution with Simple Approach

import unittest

def mostCommonWord(paragraph, banned):

    dic = {}
    for ch in "!?',;.":
        paragraph = paragraph.replace(ch, " ")
    p = paragraph.lower().split()

    for word in p:
        if word not in banned:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

    return max(dic.items(), key=lambda x:x[1])[0]


class Test(unittest.TestCase):

    def test_mostCommonWord(self):
        self.assertEqual(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]), "ball")
        self.assertEqual(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["bob"]), "hit")
        self.assertEqual(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.:;", ["bob"]), "hit")
        self.assertEqual(mostCommonWord("bob, ball, BALL.", ["bob"]), "ball")


if __name__ == "__main__":

    unittest.main()
