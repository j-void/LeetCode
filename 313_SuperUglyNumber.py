from heapq import *
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # heap = [1]
        # visited = set([1])
        # while heap:
        #     num = heappop(heap)
        #     if n == 1:
        #         return num
        #     for p in primes:
        #         cnum = p * num
        #         if cnum not in visited:
        #             heappush(heap, cnum)
        #             visited.add(cnum)
        #     n -= 1

        idx = [0] * len(primes)
        current_state = primes[:]
        output = [1] * n
        for i in range(1, n):
            curr_min = min(current_state)
            output[i] = curr_min

            for j in range(len(primes)):
                if curr_min == current_state[j]:
                    idx[j] += 1
                    current_state[j] = primes[j] * output[idx[j]]

        return output[-1]
            

