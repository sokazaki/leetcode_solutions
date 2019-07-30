# O(N) Solution with Postorder Traversal (with Pruning)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):

        if not root:
            return 0

        def postorder(node, minval, maxval):
            sumval = 0
            if maxval > L and node.left:
                sumval += postorder(node.left, minval, node.val)
            if minval < R  and node.right:
                sumval += postorder(node.right, node.val, maxval)

            if L <= node.val <= R:
                sumval += node.val
            return sumval

        return postorder(root, float("-inf"), float("inf"))
