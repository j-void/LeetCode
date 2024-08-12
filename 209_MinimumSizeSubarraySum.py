class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        running_sum = 0
        start = 0
        min_length = float('inf')
        for i in range(len(nums)):
            running_sum += nums[i]

            while running_sum >= target:
                min_length = min(min_length, i-start+1)
                running_sum -= nums[start]
                start += 1

        

        return 0 if min_length == float('inf') else min_length
