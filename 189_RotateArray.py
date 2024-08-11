class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     k = k % len(nums)
    #     if k == 0 or len(nums)==1 or len(nums)==k:
    #         return
    #     bk = nums[:-k]
    #     nums[:k] = nums[-k:]
    #     nums[k:] = bk
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0 or len(nums)==1 or len(nums)==k:
            return
        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
