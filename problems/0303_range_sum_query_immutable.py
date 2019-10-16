class NumArray():
    def __init__(self, nums):
        self.cumsum = [0]
        for num in nums:
            self.cumsum.append(self.cumsum[-1] + num)
        
    def sumRange(self, i, j):
        return self.cumsum[j+1] - self.cumsum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
