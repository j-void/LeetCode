import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        l = math.log10(n) / math.log10(3)
        return l == int(l)
