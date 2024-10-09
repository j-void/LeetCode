"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def is_uniform(self, grid):
        first_val = grid[0][0]
        for row in grid:
            for cell in row:
                if cell != first_val:
                    return False
        return True

    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)

        if n == 1 or self.is_uniform(grid):
            return Node(val=grid[0][0], isLeaf=True)

        mid = n // 2
        
        topLeft = self.construct([row[:mid] for row in grid[:mid]])
        topRight = self.construct([row[mid:] for row in grid[:mid]])
        bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
        bottomRight = self.construct([row[mid:] for row in grid[mid:]])

        if not topLeft and not topRight and not bottomLeft and not bottomRight and (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(val=topLeft.val, isLeaf=True)


        return Node(val=1, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
