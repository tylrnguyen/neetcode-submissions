# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1
        
    
    def dfs(self, root): 
        if root is None: 
            return 0

        height_left = self.dfs(root.left)
        if height_left == -1: 
            return -1
        height_right = self.dfs(root.right)
        if height_right == -1: 
            return -1

        diff = abs(height_left - height_right)

        if diff > 1: 
            return -1
        
        return 1 + max(height_left, height_right)