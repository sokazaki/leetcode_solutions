# O(1) Time Complexity / O(N) Space Complexity Solution with Simple Approach

class TicTacToe:

    def __init__(self, n):
        self.n = n
        self.rowtable = [0]*n
        self.coltable = [0]*n
        self.diag1 = 0
        self.diag2 = 0
        
    def move(self, row, col, player):
        if player == 1:
            p = 1
        elif player == 2:
            p = -1
        
        self.rowtable[row] += p
        self.coltable[col] += p
        if row == col: self.diag1 += p
        if (self.n-1-row) == col: self.diag2 += p
                
        if abs(self.rowtable[row]) == self.n or abs(self.coltable[col]) == self.n or abs(self.diag1) == self.n or abs(self.diag2) == self.n:
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
