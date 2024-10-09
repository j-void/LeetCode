"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        output = []
        while queue:
            curr = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                curr.append(node.val)
                for c in node.children:
                    queue.append(c)
            output.append(curr)

        return output
