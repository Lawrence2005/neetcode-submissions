# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, None)
    
    def helper(self, root, cummax):
        if not root:
            return 0
        
        isGood = 1 if not cummax or root.val >= cummax else 0

        cummax = max(cummax, root.val) if cummax else root.val
        left = self.helper(root.left, cummax)
        right = self.helper(root.right, cummax)
        return isGood + left + right