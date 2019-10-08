# O(NlogK) Solution with Priority Queue

from collections import deque

class MovingAverage:

    def __init__(self, size):
        self.queue = deque(maxlen=size)

    def next(self, val):
        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
