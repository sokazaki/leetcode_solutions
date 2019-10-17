import heapq


class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num):
        if len(self.small_heap) == len(self.large_heap):
            candidate = -heapq.heappushpop(self.small_heap, -num)
            heapq.heappush(self.large_heap, candidate)
        else:
            candidate = -heapq.heappushpop(self.large_heap, num)
            heapq.heappush(self.small_heap, candidate)

    def findMedian(self):
        if len(self.small_heap) == len(self.large_heap):
            return float(self.large_heap[0] - self.small_heap[0]) / 2
        else:
            return float(self.large_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
