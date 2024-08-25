class Solution:
    def addDigits(self, num: int) -> int:

        def helper(num):
            digit_sum = 0
            while num:
                digit = num % 10
                num = num // 10
                digit_sum += digit
            return digit_sum
        
        while num % 10 != num:
            num = helper(num)
        
        return num
        
