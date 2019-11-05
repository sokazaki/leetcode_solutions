# O(1) push/pop/top/peekMax, O(N) popMax Time Complexity / O(N) Space Complexity Solution with Two Stack

class MaxStack:

    def __init__(self):
        self.stack=[]
        self.maxstack=[]

    def push(self, x):
        self.stack.append(x)
        if not self.maxstack:
            self.maxstack.append(x)
        else:
            self.maxstack.append(max(x, self.maxstack[-1]))

    def pop(self):
        self.maxstack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.maxstack[-1]

    def popMax(self):
        n = self.maxstack.pop()
        i = len(self.stack)-1
        tmp = []
        while n != self.stack[-1]:
            tmp.append(self.pop())
        res = self.stack.pop()
        for i in range(len(tmp)-1, -1, -1):
            self.push(tmp[i])
        return res


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
