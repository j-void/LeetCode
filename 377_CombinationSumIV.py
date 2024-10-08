class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for t in range(1, target+1):
            for n in nums:
                if t >= n:
                    dp[t] = dp[t] + dp[t-n]

        return dp[-1]
