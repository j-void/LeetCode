from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heappush(heap, nums[i])
        
        for i in range(k, len(nums)):
            if heap[0] < nums[i]:
                heappop(heap)
                heappush(heap, nums[i])
        
        return heap[0]
        
