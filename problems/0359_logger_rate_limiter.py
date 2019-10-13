# Memory Efficient Solution with Queue

from collections import deque

class Logger:

    def __init__(self):
        self.queue = deque()

    def shouldPrintMessage(self, timestamp, message):
        while self.queue and timestamp - self.queue[0][0] >= 10:
            self.queue.popleft()
        
        for _, past_message in self.queue:
            if message in past_message:
                return False
        
        self.queue.append((timestamp, message))
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
