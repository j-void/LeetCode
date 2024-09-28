class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        start = 1
        end = 9
        while n > digit_length*end:
            n -= digit_length*end
            digit_length += 1
            start *= 10
            end *= 10
        
        num = start + (n-1)//digit_length
        digit_index = (n-1) % digit_length

        return int(str(num)[digit_index])
        
