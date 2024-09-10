class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
