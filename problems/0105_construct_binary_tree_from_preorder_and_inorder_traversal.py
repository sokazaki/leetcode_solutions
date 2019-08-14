# O(N) Solution with DFS


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):

    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])

        return root
