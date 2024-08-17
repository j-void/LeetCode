class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        max_area = 0

        for i in range(rows):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
            max_area = max(max_area, dp[i][0])
        
        for i in range(cols):
            dp[0][i] = 1 if matrix[0][i] == "1" else 0
            max_area = max(max_area, dp[0][i])

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                max_area = max(max_area, dp[i][j])

        return max_area**2
