# O(NL) Solution with Bidirectional BFS (N: The length of wordList, L: The length of Each Word)

import unittest
from string import ascii_lowercase


def ladderLength(beginWord, endWord, wordList):

    wordList = set(wordList)

    if endWord not in wordList:
        return 0

    if beginWord in wordList:
        wordList.remove(beginWord)

    head, tail = {beginWord}, {endWord}
    res = 1

    while head and tail:
        if len(head) > len(tail):
            head, tail = tail, head
        queue = set()
        while head:
            word = head.pop()
            for i in range(len(beginWord)):
                prefix, suffix = word[:i], word[i+1:]
                for c in ascii_lowercase:
                    candidate = prefix + c + suffix

                    if candidate in tail:
                        return res + 1
                    if candidate in wordList:
                        queue.add(candidate)
                        wordList.remove(candidate)
        res += 1
        head = queue

    return 0


class Test(unittest.TestCase):

    def test_ladderLength(self):
        self.assertEqual(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(ladderLength("hit", "cug", ["hot","dot","dog","lot","log","cog"]), 0)
        self.assertEqual(ladderLength("hit", "cog", ["hat","dot","dog","lot","log","cog"]), 0)
        self.assertEqual(ladderLength("hit", "cog", ["hut","dut","dot","lot","log","cog"]), 7)
        self.assertEqual(ladderLength("hit", "cog", ["hit", "hut","dut","dot","lot","log","cog"]), 7)
        self.assertEqual(ladderLength("a", "c", ["b", "c"]), 2)
        self.assertEqual(ladderLength("a", "c", ["a", "b", "c"]), 2)

if __name__ == "__main__":

    unittest.main()
