class Solution:

    def integerReplacement(self, n: int) -> int:
        dp = {1:0}
        def helper(i):
            if i in dp:
                return dp[i]

            if i % 2 == 0:
                dp[i] = helper(i//2) + 1
            else:
                dp[i] = min(helper((i+1)//2), helper((i-1)//2)) + 2
            
            return dp[i]

        return helper(n)
