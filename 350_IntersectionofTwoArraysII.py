class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = defaultdict(int)
        nums2_dict = defaultdict(int)
        for n in nums1:
            nums1_dict[n] += 1
        for n in nums2:
            nums2_dict[n] += 1
        output = []
        for k,v in nums1_dict.items():
            if k in nums2_dict:
                output += [k] * min(v, nums2_dict[k])
        
        return output
        
