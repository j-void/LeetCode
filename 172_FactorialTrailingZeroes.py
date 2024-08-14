class Solution:
    def trailingZeroes(self, n: int) -> int:
        output = 0
        p5 = 5
        while n//p5 > 0:
            output += n//p5
            p5 *= 5
        
        return output
