# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(node, n, tlist):
            if not node:
                return
            tlist.append(node)
            if n == node:
                return 
            if n.val < node.val:
                search(node.left, n, tlist)
            else:
                search(node.right, n, tlist)
        
        p_list = []
        q_list = []

        search(root, p, p_list)
        search(root, q, q_list)
        
        i, j = 0, 0
        common = root
        while i < len(p_list) and j < len(q_list):
            if p_list[i].val != q_list[j].val:
                break
            common = p_list[i]
            i += 1
            j += 1

        return common
        
