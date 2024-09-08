class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()
        def helper(wx, wy):
            if wx + wy == target:
                return True
            if (wx, wy) in visited:
                return False
            visited.add((wx, wy))

            output = False

            ## fill them
            output = output or helper(x, wy)
            output = output or helper(wx, y)

            ## empty
            output = output or helper(wx, 0)
            output = output or helper(0, wy)

            ## transfer
            output = output or helper(min(x, wx+wy), max(0, wy - max(0, x-wx)))
            output = output or helper(max(0, wx - max(0, y-wy)), min(y, wx+wy))
            return output
        
        return helper(0,0)
