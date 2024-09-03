class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = {}  

        def dfs(i, j, prev_val):
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= prev_val:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            up = dfs(i-1, j, matrix[i][j])
            down = dfs(i+1, j, matrix[i][j])
            left = dfs(i, j-1, matrix[i][j])
            right = dfs(i, j+1, matrix[i][j])

            dp[(i, j)] = 1 + max(up, down, left, right)
            return dp[(i, j)]

        max_len = 0
        for i in range(rows):
            for j in range(cols):
                max_len = max(max_len, dfs(i, j, -float('inf')))

        return max_len
            
            
