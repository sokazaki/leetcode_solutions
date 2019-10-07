# O(N) Solution with Recursive and Iterative(BFS) Approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_recursive:
    def isSymmetric(self, root):
        if not root:
            return True
        else:
            return self.helper(root.left, root.right)
    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            outer = self.helper(left.left, right.right)
            inner = self.helper(left.right, right.left)
            return outer and inner
        else:
            return False

from collections import deque
class Solution_iterative:
    def isSymmetric(self, root):
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            elif (not left or not right) or (left.val != right.val):
                return False

            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True
