# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        return self.helper(root,float('-inf'), float('inf'))
    
    def helper(self, root, l, r):
        if not root:
            return True
        return l<root.val<r and self.helper(root.left, l, root.val) and self.helper(root.right, root.val, r)
