# O(1) Time Complexity / O(1) Space Complexity Solution with Simple Approach

class HitCounter:

    def __init__(self):
        self.counter = [[0,i+1] for i in range(300)]

    def hit(self, timestamp):
        idx = (timestamp-1)%300
        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx][1] = timestamp
            self.counter[idx][0] = 1


    def getHits(self, timestamp):
        res = 0
        for x in self.counter:
            if timestamp-x[1] < 300:
                res += x[0]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
