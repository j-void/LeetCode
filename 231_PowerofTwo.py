class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n:
            if n % 2 != 0 and n!= 1:
                return False
            n = n // 2
        return True
