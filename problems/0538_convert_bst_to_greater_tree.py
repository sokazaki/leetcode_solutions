# O(N) Solution with DFS (reverse inorder)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        self.val = 0
        def dfs(root):
            if root:
                dfs(root.right)
                root.val += self.val
                self.val = root.val
                dfs(root.left)
        dfs(root)
        return root
