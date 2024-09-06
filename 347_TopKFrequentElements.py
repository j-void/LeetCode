from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        for n in nums:
            count_dict[n] += 1
        heap = []
        i = 0
        for key,v in count_dict.items():
            if i < k:
                heappush(heap, (v, key))
            else:
                if heap[0][0] < v:
                    heappop(heap)
                    heappush(heap, (v, key))
            i += 1
        return [h[1] for h in heap]
