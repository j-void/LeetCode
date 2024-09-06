class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_set = set(nums2)
        output = set()
        for n in nums1:
            if n in nums2_set:
                output.add(n)
        
        return list(output)
        
