from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i, j = 0, 0
        heap = []
        output = []
        for i in range(min(k, len(nums1))):
            heappush(heap, (nums1[i]+nums2[0], (i,0)))
        
        while heap and k > 0:
            _, (i,j) = heappop(heap)

            if j < len(nums2)-1:
                heappush(heap, (nums1[i]+nums2[j+1], (i,j+1)))
            
            output.append([nums1[i], nums2[j]])
            k -= 1
        
        return output
            
