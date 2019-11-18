import random

class Solution:

    def __init__(self, n_rows, n_cols):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.end = self.n_rows * self.n_cols - 1
        self.dict = {}
        
    def flip(self):
        rand = random.randint(0, self.end)
        res = self.dict.get(rand, rand)
        self.dict[rand] = self.dict.get(self.end, self.end)
        self.end -= 1
        return divmod(res, self.n_cols)
    
    def reset(self):
        self.dict = {}
        self.end = self.n_rows * self.n_cols - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
