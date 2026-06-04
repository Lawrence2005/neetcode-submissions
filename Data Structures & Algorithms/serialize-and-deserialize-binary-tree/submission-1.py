# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.result = []
        self.serializeHelper(root)
        return ' '.join(self.result)

    def serializeHelper(self, root):
        if not root:
            self.result.append('N')
            return
        
        self.result.append(str(root.val))
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

        curr = self.data[self.i]
        self.i += 1

        if curr == 'N':
            return None

        root = TreeNode(curr)
        root.left = self.deserializeHelper()
        root.right = self.deserializeHelper()

        return root