class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        for _ in range(32):
            lsb = n & 1
            output += lsb
            n = n >> 1
        return output
