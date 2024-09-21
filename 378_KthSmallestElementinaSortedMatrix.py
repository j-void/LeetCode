from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heappop(heap)
        
        return -heap[0]
