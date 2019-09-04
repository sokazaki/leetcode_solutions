# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        res = []

        def preOrder(node):
            if not node:
                return
            res.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, res))

    def deserialize(self, data):
        vals = deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
