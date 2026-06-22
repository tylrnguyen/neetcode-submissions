# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = [] 
        queue = [root]

        result = []
        while queue and root is not None: 
            for node in queue: 
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            # the last node in curr level is the last value in queue 
            result.append(queue[-1].val)    
            queue = level
            level = []
        return result