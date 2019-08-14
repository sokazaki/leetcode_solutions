# O(N) Solution with DFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(inorder, postorder):

    if inorder:
        idx = inorder.index(postorder.pop())
        root = TreeNode(inorder[idx])
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)

        return root
