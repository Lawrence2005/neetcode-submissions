# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        inorderMap = {inorder[i]: i for i in range(len(inorder))}
        preinInMap = {preorder[i]: inorderMap[preorder[i]] for i in range(len(preorder))}

        root = TreeNode(preorder[0])

        preIndex = preinInMap[preorder[0]]

        root.left = self.buildTree(preorder[1:preIndex + 1], inorder[:preIndex])
        root.right = self.buildTree(preorder[preIndex + 1:], inorder[preIndex + 1:])
        return root