class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0]*len(prices) for _ in range(1+k)]

        for t in range(1, 1+k):
            buy = -prices[0]
            for i in range(1, len(prices)):
                dp[t][i] = max(dp[t][i-1], buy+prices[i])
                buy = max(buy, dp[t-1][i]-prices[i])
        return dp[-1][-1]
