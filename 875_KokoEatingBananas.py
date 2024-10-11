import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        def has_eaten(k):
            ch = 0
            for p in piles:
                c = math.ceil(p/k)
                ch += c

            return ch
        output = -1
        left, right = 1, max(piles)
        while left <= right:
            mid = (left+right)//2
            curr = has_eaten(mid)
            if curr <= h:
                output = mid
                right = mid - 1
            else:
                left = mid + 1

        return output   
