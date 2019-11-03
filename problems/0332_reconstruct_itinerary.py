# O(N) Solution with DFS

import unittest

def findItinerary(tickets):
    dic = {}
    for src, dst in tickets:
        if src in dic:
            dic[src].append(dst)
        else:
            dic[src] = [dst]

    for src in dic.keys():
        dic[src].sort(reverse=True)
    stack = []
    res = []
    stack.append("JFK")

    while len(stack) > 0:
        airport = stack[-1]
        if airport in dic and len(dic[airport]) > 0:
            stack.append(dic[airport].pop())
        else:
            res.append(stack.pop())

    return res[::-1]

class Test(unittest.TestCase):

    def test_findItinerary(self):
        self.assertEqual(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]), ["JFK", "MUC", "LHR", "SFO", "SJC"])
        self.assertEqual(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]), ["JFK","ATL","JFK","SFO","ATL","SFO"])
        self.assertEqual(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFC", "SJC"], ["LHR", "SFC"]]), ["JFK", "MUC", "LHR", "SFC", "SJC"])


if __name__ == "__main__":

    unittest.main()
