# O(N) Solution with BFS or DFS

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_bfs:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([[p, q]])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append([node1.left, node2.left])
                queue.append([node1.right, node2.right])
        return True
        
 
