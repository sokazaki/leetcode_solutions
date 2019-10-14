# O(N) Solution with Stack

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]

        while stack:
            cur, curstr = stack.pop()
            if not cur.left and not cur.right:
                res.append(curstr+str(cur.val))
            if cur.right:
                stack.append((cur.right, curstr+str(cur.val)+"->"))
            if cur.left:
                stack.append((cur.left, curstr+str(cur.val)+"->"))

        return res
