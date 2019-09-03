# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):    
        if not root:
            return None
        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else '#')

        return ','.join(res)
                
    
    def deserialize (self, data):
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        idx = 1

        while q:
            node = q.popleft()
            if nodes[idx] is not '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
        
            if nodes[idx] is not '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
