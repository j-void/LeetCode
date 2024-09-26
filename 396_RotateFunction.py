class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        total_sum = sum(nums)
        curr_sum = sum(i * nums[i] for i in range(n)) 
        max_value = curr_sum

        for i in range(1, n):
            curr_sum = curr_sum + total_sum - n * nums[-i]
            max_value = max(max_value, curr_sum)
        
        return max_value
