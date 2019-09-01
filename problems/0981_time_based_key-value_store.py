from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        v = self.dic.get(key)
        i = bisect.bisect_right(v, [timestamp, chr(ord('z')+1)])
        return v[i-1][1] if i else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
