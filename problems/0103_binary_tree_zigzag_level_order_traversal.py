# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):

        res, queue = [], [(root, 0)]

        while queue:
            cur, level = queue.pop(0)
            if cur:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(cur.val)
                else:
                    res[level].insert(0, cur.val)

                queue.append((cur.left, level+1))
                queue.append((cur.right, level+1))

        return res
