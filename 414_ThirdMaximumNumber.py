from heapq import *
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = [-n for n in set(nums)]
        heapify(nums)
        if len(nums) < 3:
            return -nums[0]
        i = 3
        output = 0
        while i >= 1:
            output = -heappop(nums)
            i -= 1
        return output
