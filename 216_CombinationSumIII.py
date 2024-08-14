class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i+1 for i in range(9)]
        output = []
        def helper(j, curr_sum, curr_arr):
            if curr_sum == 0 and len(curr_arr)==k:
                output.append(curr_arr)
                return
            
            for i in range(j, len(nums)):
                if curr_sum - nums[i] >= 0 and len(curr_arr)<k:
                    helper(i+1, curr_sum - nums[i], curr_arr+[nums[i]])
        helper(0, n, [])

        return output
