# O(N) Push / O(1) Pop, Peek(Top), IsEmpty Solution with Two Stacks

class MyQueue:

    def __init__(self):
        self.master = []
        self.slave = []

    def push(self, x: int):
        while len(self.master):
            top = self.master.pop()
            self.slave.append(top)
        self.master.append(x)
        while len(self.slave):
            top = self.slave.pop()
            self.master.append(top)

    def pop(self):
        return self.master.pop()

    def peek(self):
        return self.master[-1]

    def empty(self):
        return not len(self.master)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
