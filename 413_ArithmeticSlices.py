class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        output = 0
        start = 0
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            cdiff = nums[i] - nums[i-1]
            if cdiff != diff:
                diff = cdiff
                start = i-1
            else:
                output += 1
                j = start+1
                while i-j >= 2:
                    output += 1
                    j += 1
        return output
