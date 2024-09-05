class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        if n == 2:
            return 1
        if n == 3:
            return 2
        ## if 2 or 3 then don't split it
        dp[2], dp[3] = 2, 3
        for i in range(4, n+1):
            dp[i] = max(dp[2] * dp[i - 2], dp[3] * dp[i - 3])
        
        return dp[-1]
        
        
