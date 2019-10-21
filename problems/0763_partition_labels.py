# O(N) Solution with Two Pointers

import unittest


def partitionLabels(S):

    dic = {letter: i for i, letter in enumerate(S)}
    left, right, res = 0, 0, []

    for i, letter in enumerate(S):

        right = max(right, dic[letter])

        if i == right:
            res.append(right-left+1)
            left = i+1

    return res


class Test(unittest.TestCase):

    def test_partitionLabels(self):
        self.assertEqual(partitionLabels("ababcbacadefegdehijhklij"), [9,7,8])
        self.assertEqual(partitionLabels("ababcbacwdefegdehijhklij"), [8,1,7,8])
        self.assertEqual(partitionLabels("ababcczxwdefegdehijhklij"), [4,2,1,1,1,7,8])
        self.assertEqual(partitionLabels("a"), [1])
        self.assertEqual(partitionLabels("abcdefghijkla"), [13])


if __name__ == "__main__":

    unittest.main()
