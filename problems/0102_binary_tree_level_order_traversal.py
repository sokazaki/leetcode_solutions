from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):

        res, queue = [], deque([(root, 0)])
        while queue:
            cur, level = queue.popleft()
            if cur:
                if len(res) < level+1:
                    res.append([])
                res[level].append(cur.val)
                queue.append((cur.left, level+1))
                queue.append((cur.right, level+1))

        return res
