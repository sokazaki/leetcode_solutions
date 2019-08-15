# O(4^N/sqrt(N)) Solution with DFS (Backtracking)

import unittest


class Solution:
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, res = n, n, []
        self.dfs(left, right, res, "")
        return res

    def dfs(self, left, right, res, string):
        if right < left:
            return
        if not left and not right:
            res.append(string)
            return
        if left:
            self.dfs(left-1, right, res, string + "(")
        if right:
            self.dfs(left, right-1, res, string + ")")


class Test(unittest.TestCase):

    def test_generateParenthesis(self):
        ans = Solution()
        self.assertEqual(ans.generateParenthesis(0), [])
        self.assertEqual(ans.generateParenthesis(1), ["()"])
        self.assertEqual(ans.generateParenthesis(2), ["(())","()()"])
        self.assertEqual(ans.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])
        self.assertEqual(ans.generateParenthesis(4), ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])

if __name__ == "__main__":

    unittest.main()
