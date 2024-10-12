class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        prefix_sum = 0
        prefix_sum_dict = defaultdict(int)
        prefix_sum_dict[0] = 1
        for num in nums:
            prefix_sum += num 
            output += prefix_sum_dict[prefix_sum - k]
            prefix_sum_dict[prefix_sum] += 1

        return output
        
        
