from heapq import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = []
        for k,v in count.items():
            heappush(heap, (-v, k))
        output = ""
        while len(heap) > 1:
            v1, k1 = heappop(heap)
            v2, k2 = heappop(heap)
            v = 1
            output += (k1+k2)*v
            v1 += v
            if v1:
                heappush(heap, (v1, k1)) 
            v2 += v
            if v2:
                heappush(heap, (v2, k2)) 
        if heap:
            v,k = heappop(heap)
            if (output and output[-1] == k) or -v > 1:
                return ""
            output += k*(-v)
        return output

            
