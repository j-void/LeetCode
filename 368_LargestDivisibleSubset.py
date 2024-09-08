class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) <= 1:
            return nums
        dp = [[num] for num in nums]
        max_len = 0
        max_idx = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(dp[i])<len(dp[j])+1:
                    dp[i] = dp[j] + [nums[i]]

                    if len(dp[i]) > max_len:
                        max_len = len(dp[i])
                        max_idx = i
        return dp[max_idx]

        
