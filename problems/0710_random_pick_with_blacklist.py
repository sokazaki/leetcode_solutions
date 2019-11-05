import random

class Solution:

    def __init__(self, N, blacklist):

        blacklist = set(blacklist)
        self.length = N - len(blacklist)
        self.remap = {}
        remap_list = []
        for num in blacklist:
            if num < self.length:
                remap_list.append(num)
        j = 0
        for i in range(self.length, N):
            if i not in blacklist:
                self.remap[remap_list[j]] = i
                j += 1
            
    def pick(self):

        idx = random.randint(0, self.length-1)
        return self.remap[idx] if idx in self.remap else idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
