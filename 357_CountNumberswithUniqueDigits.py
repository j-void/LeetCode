class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1;
        if n == 1: return 10;
        value = 9
        for i in range(2, n+1):
            value *= (11-i)
        return value + self.countNumbersWithUniqueDigits(n-1)

    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     if n == 0: return 1;
    #     total = 10
    #     prod = 9
    #     for i in range(2, n+1):
    #         total += (prod * (11-i))
    #         prod *= (11-i)
    #     return total
