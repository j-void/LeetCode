# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        left_height, right_height = 0,0
        node = root
        while node:
            left_height += 1
            node = node.left
        node = root
        while node:
            right_height += 1
            node = node.right
        if left_height == right_height:
            return 2**left_height - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

            
        
        
