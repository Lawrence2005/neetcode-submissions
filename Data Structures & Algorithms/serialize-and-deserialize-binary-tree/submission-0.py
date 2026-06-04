# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        self.serializeHelper(root)
        return ' '.join(self.res)

    def serializeHelper(self, root):
        if not root:
            self.res.append('N')
            return
        
        self.res.append(str(root.val))
        self.serializeHelper(root.left)
        self.serializeHelper(root.right)
        return
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.data = data.split()
        self.i = 0
        return self.deserializeHelper()
    
    def deserializeHelper(self):
        if self.i >= len(self.data):
            return None
        
        node = self.data[self.i]
        self.i += 1

        if node == 'N':
            return None
        
        root = TreeNode(int(node))
        root.left = self.deserializeHelper()
        root.right = self.deserializeHelper()

        return root