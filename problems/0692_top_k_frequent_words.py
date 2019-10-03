# O(NlogK) Time Complexity / O(N) Space Complexity Solution with Priority Queue

import unittest
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, Word(val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]


class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word


class Test(unittest.TestCase):

    def test_topKFrequent(self):
        ans = Solution()
        self.assertEqual(ans.topKFrequent(["i","love","leetcode","i","love","coding"], 2), ["i","love"])
        self.assertEqual(ans.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4), ["the","is","sunny","day"])
        self.assertEqual(ans.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 3), ["the","is","sunny"])
        self.assertEqual(ans.topKFrequent(["i","love","leetcode","i","love","i"], 1), ["i"])
        self.assertEqual(ans.topKFrequent(["i"], 1), ["i"])

if __name__ == "__main__":

    unittest.main()
