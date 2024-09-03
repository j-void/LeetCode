class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        mid = (n-1)//2
        left_half = nums[:mid+1]  
        right_half = nums[mid+1:]
        left_half.reverse()
        right_half.reverse()
    
        for i in range(len(left_half)):
            nums[2 * i] = left_half[i]  
        for i in range(len(right_half)):
            nums[2 * i + 1] = right_half[i]
        
