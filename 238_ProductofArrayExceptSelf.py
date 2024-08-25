class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        suffix = [nums[-1]] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(suffix[i+1])
            elif i == len(nums)-1:
                output.append(prefix[-2])
            else:
                output.append(prefix[i-1]*suffix[i+1])
        return output
        
