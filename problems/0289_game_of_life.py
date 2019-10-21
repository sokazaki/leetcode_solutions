# O(NM) Time Complexity / O(1) Space Complexity Solution with Simple Approach

import unittest

def gameOfLife(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            count = 0
            for row in range(max(0, i-1), min(i+2, len(board))):
                for col in range(max(0, j-1), min(j+2, len(board[0]))):
                    if (row, col) != (i, j) and 1 <= board[row][col] <= 2:
                        count += 1
            if board[i][j] == 0:
                if count == 3:
                    board[i][j] = 3
            else:
                if count < 2 or count > 3:
                    board[i][j] = 2

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                board[i][j] = 0
            elif board[i][j] == 3:
                board[i][j] = 1

    return board


class Test(unittest.TestCase):

    def test_gameOfLife(self):
        self.assertEqual(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]), [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
        self.assertEqual(gameOfLife([[0,1,0,1],[0,0,1,0],[1,1,1,0],[0,0,0,1]]), [[0,0,1,0],[1,0,0,1],[0,1,1,1],[0,1,1,0]])
        self.assertEqual(gameOfLife([[0,1,0,1]]), [[0,0,0,0]])
        self.assertEqual(gameOfLife([[0,1,0,1],[0,0,1,0],[1,1,1,0],[0,0,0,1],[1,1,1,0]]), [[0,0,1,0],[1,0,0,1],[0,1,1,1],[0,0,0,1],[0,1,1,0]])
        self.assertEqual(gameOfLife([[1]]), [[0]])

if __name__ == "__main__":

    unittest.main()
