class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0;
        low, high = min(nums), max(nums)
        B = collections.defaultdict(list)
        for n in nums:
            if n == high:
                idx = len(nums)-1
            else:
                idx = ((n-low)*(len(nums)-1))//(high-low)
            B[idx].append(n)
        
        buckets = []
        for i in range(len(nums)):
            if B[i]:
                buckets.append([min(B[i]), max(B[i])])

        mdiff = 0
        for i in range(1, len(buckets)):
            mdiff = max(mdiff, abs(buckets[i-1][-1]-buckets[i][0]))

        return mdiff
