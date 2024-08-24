class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return ""
        output = []
        start = nums[0]
        nums.append(nums[-1]+2)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if nums[i-1] == start:
                    output.append(str(start))
                else:
                    output.append(str(start)+"->"+str(nums[i-1]))
                start = nums[i]
        return output
