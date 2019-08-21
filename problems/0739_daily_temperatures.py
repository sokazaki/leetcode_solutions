import unittest

def dailyTemperatures(T):
    res = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            res[cur] = i - cur
        stack.append(i)

    return res

class Test(unittest.TestCase):

    def test_dailyTemperatures(self):
        self.assertListEqual(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertListEqual(dailyTemperatures([73, 74, 75, 71, 69, 72, 71, 73]), [1, 1, 0, 2, 1, 2, 1, 0])
        self.assertListEqual(dailyTemperatures([73, 74, 75, 71]), [1, 1, 0, 0])
        self.assertListEqual(dailyTemperatures([]), [])

if __name__ == "__main__":

    unittest.main()
