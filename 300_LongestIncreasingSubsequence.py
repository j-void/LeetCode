class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(num):
            left, right = 0, len(res)-1
            while left <= right:
                mid = (left+right)//2
                if res[mid] < num:
                    left = mid + 1
                elif res[mid] > num:
                    right = mid - 1
                else:
                    return mid
            return left

        for i in range(len(nums)):
            if not res or res[-1] < nums[i]:
                res.append(nums[i])
            else:
                ri = binary_search(nums[i])
                res[ri] = nums[i]

        return len(res)        
