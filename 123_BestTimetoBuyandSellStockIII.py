from heapq import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * len(prices) for _ in range(2 + 1)]
    
        for t in range(1, 2 + 1):
            max_diff = -prices[0]
            for i in range(1, len(prices)):
                dp[t][i] = max(dp[t][i-1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[t-1][i] - prices[i])
        
        return dp[2][len(prices) - 1]
        
        
