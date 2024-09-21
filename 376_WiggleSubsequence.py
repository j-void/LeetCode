class Solution:
    # def wiggleMaxLength(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n < 2:
    #         return 1
    #     dp = [1]*n
    #     diff = [0] * n
    #     for i in range(1, n):
    #         if nums[i-1] != nums[i]:
    #             dp[i] = 2
    #         diff[i] = nums[i] - nums[i - 1]
        
    #     # diff[1] = nums[1] - nums[0]
    #     for i in range(n):
    #         for j in range(i):
    #             if 1+dp[j] > dp[i] and diff[j] * (nums[i]-nums[j]) < 0:
    #                 dp[i] = 1+dp[j]
    #                 diff[i] = nums[i]-nums[j]
    #     # print(dp)
    #     return dp[-1]
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        up = down = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1  
            elif nums[i] < nums[i-1]:
                down = up + 1  
        
        return max(up, down)
