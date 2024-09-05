import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        l = math.log(n, 4)
        return l % 1 == 0
        
