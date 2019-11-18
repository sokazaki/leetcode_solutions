# O(N) Solution with Stack

import unittest

def asteroidCollision(asteroids):

    if not asteroids:
        return []

    stack = [asteroids[0]]
    for i in asteroids[1:]:
        stack.append(i)
        while len(stack)>=2 and stack[-1] < 0 and stack[-2] > 0:
            if abs(stack[-1])>abs(stack[-2]):
                stack[-2] = stack[-1]
                stack.pop()
            elif abs(stack[-1])<abs(stack[-2]):
                stack.pop()
            elif abs(stack[-1])==abs(stack[-2]):
                stack.pop()
                stack.pop()
            if len(stack)<=1:
                break

    return stack


class Test(unittest.TestCase):

    def test_asteroidCollision(self):
        self.assertEqual(asteroidCollision([5, 10, -5]), [5, 10])
        self.assertEqual(asteroidCollision([8, -8]), [])
        self.assertEqual(asteroidCollision([10, 2, -5]), [10])
        self.assertEqual(asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])
        self.assertEqual(asteroidCollision([-2]), [-2])

if __name__ == "__main__":

    unittest.main()
