class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:return -1;
        curr_min = float('inf')
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            curr_min = min(curr_min, nums[left], nums[mid], nums[right])
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return curr_min
        
