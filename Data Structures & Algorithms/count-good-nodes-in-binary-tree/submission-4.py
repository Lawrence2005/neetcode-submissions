# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        self.helper(root, float('-inf'))
        return self.count
    
    def helper(self, root, currMax):
        if not root:
            return
        
        if root.val >= currMax:
            self.count += 1
        currMax = max(currMax, root.val)

        self.helper(root.left, currMax)
        self.helper(root.right, currMax)
        return