class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = nums[0]
        mid = float('inf')
        for i in range(1, len(nums)):
            if mid != float('inf') and nums[i] > mid:
                return True
            if nums[i] < left:
                left = nums[i]
                continue
            if nums[i] < mid and nums[i] != left:
                mid = nums[i]
                continue
        return False
            
