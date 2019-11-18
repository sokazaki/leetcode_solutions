# O(N) Solution with Tree Traversal

import unittest


def findSmallestRegion(regions, region1, region2):
    graph = {}
    for v in regions:
        for x in v[1:]:
            graph[x] = v[0]

    tmp1 = []
    while region1 in graph:
        tmp1.append(region1)
        region1 = graph[region1]
    tmp1.append(region1)

    tmp2 = []
    while region2 in graph:
        tmp2.append(region2)
        region2 = graph[region2]
    tmp2.append(region2)

    for x in tmp1:
        if x in tmp2:
            return x


class Test(unittest.TestCase):

    def test_findSmallestRegion(self):
        self.assertEqual(findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "New York"), "North America")
        self.assertEqual(findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "Ontario"), "Canada")
        self.assertEqual(findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "Canada"), "Canada")
        self.assertEqual(findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "Brazil"), "Earth")
        self.assertEqual(findSmallestRegion([["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]], "Quebec", "South America"), "Earth")

if __name__ == "__main__":

    unittest.main()
