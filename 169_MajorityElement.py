class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_num, max_count = nums[0], 1
        for i in range(1, len(nums)):
            if max_count == 0:
                max_num = nums[i]
            
            if nums[i] == max_num:
                max_count += 1
            else:
                max_count -= 1
        
        return max_num
