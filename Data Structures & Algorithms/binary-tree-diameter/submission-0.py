# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
       
    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.count = max(self.count, left + right)
        return 1 + max(left, right)
        
       