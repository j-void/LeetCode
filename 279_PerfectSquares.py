class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        for i in range(1, n+1):
            curr_min = float('inf')
            j = 1
            while j**2 <= i:
                if j**2 == i:
                    curr_min = 1
                curr_min = min(curr_min, i//(j**2)+dp[i%(j**2)])
                j += 1
            dp[i] = curr_min

        return dp[-1]
