# O(1) Solution with Hashmap


import random

class RandomizedSet:

    def __init__(self):
        self.nums_list = []
        self.nums_map = {}
        
    def insert(self, val):
        if val not in self.nums_map:
            self.nums_list.append(val)
            self.nums_map[val] = len(self.nums_list)-1
            return True
        return False
        

    def remove(self, val):
        if val in self.nums_map:
            idx = self.nums_map[val]
            last = self.nums_list[-1]
            self.nums_list[idx]= last
            self.nums_map[last] = idx
            self.nums_list.pop()
            self.nums_map.pop(val)
            return True
        return False
            
    def getRandom(self):
        return self.nums_list[random.randint(0, len(self.nums_list)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
