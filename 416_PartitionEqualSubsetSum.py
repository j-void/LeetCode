class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum//2

        dp = [[False] * (target + 1) for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for t in range(1, target+1):
                if t >= nums[i]:
                    dp[i][t] = dp[i-1][t] or dp[i-1][t-nums[i]]
                else:
                    dp[i][t] = dp[i-1][t]

        return dp[-1][-1]
