# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            if not node.left and not node.right:
                return node.val, 0
            
            left_val, left_child_val = dfs(node.left)
            right_val, right_child_val = dfs(node.right)

            return max(node.val+left_child_val+right_child_val, left_val+right_val), left_val+right_val
        
        

        return dfs(root)[0]
