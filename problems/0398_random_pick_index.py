# O(N) Time Complexity / O(1) Space Complexity Solution with Reservoir Sampling

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
