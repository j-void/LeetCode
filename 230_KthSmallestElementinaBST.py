# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        sorted_list = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            sorted_list.append(node.val)
            helper(node.right)

        helper(root)
        return sorted_list[k-1]

