# O(NM) Time Complexity / O(1) Space Complexity Solution with Backtracking

import unittest

class Solution:
    def exist(self, board, word):

        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True

        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if not (0<=i<len(board)) or not (0<=j<len(board[0])) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"

        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])

        board[i][j] = tmp

        return res

class Test(unittest.TestCase):

    def test_exist(self):
        ans = Solution()
        self.assertEqual(ans.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCCED"), True)
        self.assertEqual(ans.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "SEE"), True)
        self.assertEqual(ans.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCB"), False)
        self.assertEqual(ans.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], "ABCESCFSADEE"), True)


if __name__ == "__main__":

    unittest.main()
