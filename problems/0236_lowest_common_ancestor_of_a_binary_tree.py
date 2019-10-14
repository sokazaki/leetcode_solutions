# O(N) Solution with Iterative Approach

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        parent_set = set()
        cur = p
        while cur in parent:
            parent_set.add(cur)
            cur = parent[cur]
        else:
            parent_set.add(cur)
        
        cur = q
        while cur not in parent_set:
            cur = parent[cur]
        return cur
