from collections import deque

class SnakeGame:

    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food[::-1]
        self.snake = deque([[0,0]])
        self.score = 0

    def move(self, direction):

        if direction == "R":
            self.snake.append([self.snake[-1][0], self.snake[-1][1]+1])
            tmp = self.snake.popleft()
        elif direction == "L":
            self.snake.append([self.snake[-1][0], self.snake[-1][1]-1])
            tmp = self.snake.popleft()
        elif direction == "U":
            self.snake.append([self.snake[-1][0]-1, self.snake[-1][1]])
            tmp = self.snake.popleft()
        elif direction == "D":
            self.snake.append([self.snake[-1][0]+1, self.snake[-1][1]])
            tmp = self.snake.popleft()
            
        if not (0 <= self.snake[-1][0] < self.height and 0 <= self.snake[-1][1] < self.width):
            return -1
        
        if len(self.snake)>=2:
            for i in range(0, len(self.snake)-1):
                if self.snake[i] == self.snake[-1]:
                    return -1
        
        if len(self.food) == 0:
            return self.score

        if self.snake[-1] == self.food[-1]:
            self.score += 1
            self.snake.appendleft(tmp)
            self.food.pop()

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
