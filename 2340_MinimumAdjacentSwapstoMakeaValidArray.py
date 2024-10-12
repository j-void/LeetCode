class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        for min_i in range(len(nums)):
            if nums[min_i] == min_num:
                break
        for max_i in range(len(nums)-1, -1, -1):
            if nums[max_i] == max_num:
                break
        output = len(nums) - 1 - max_i + min_i
        if min_i > max_i:
            output -= 1
        return output
