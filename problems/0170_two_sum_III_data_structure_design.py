# add: O(1) / find: O(N) Solution with Hashtable

class TwoSum:
    def __init__(self):
        self.dic = dict()

    def add(self, number):
        self.dic[number] = self.dic.get(number, 0) + 1;

    def find(self, value):
        for i in self.dic.keys():
            j = value - i
            if i != j and self.dic.get(j, 0) >= 1 or i == j and self.dic.get(i) >= 2:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
