import random
import bisect

class Solution:

    def __init__(self, rects):
        self.rects, self.ranges, cum = rects, [], 0
        for x1, y1, x2, y2 in rects:
            cum += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(cum)

    def pick(self):
        x1, y1, x2, y2 = self.rects[bisect.bisect_left(self.ranges, random.randint(1, self.ranges[-1]))]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
