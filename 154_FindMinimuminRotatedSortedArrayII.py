class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        curr_min = float('inf')
        left, right = 0, len(nums)-1
        i = 0
        while left <= right:
            mid = (left+right)//2
            curr_min = min(curr_min, nums[mid], nums[left], nums[right])    
            i += 1
            if nums[mid] == nums[left]:
                left += 1
                continue
            
            if nums[mid] > nums[left]:
                left = mid+1
            else:
                right = mid-1

        return curr_min
