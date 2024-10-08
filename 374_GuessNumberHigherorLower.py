# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n
        while i <= j:
            mid = (i+j)//2
            guess_out = guess(mid)
            if guess_out == -1:
                j = mid-1
            elif guess_out == 1:
                i = mid+1
            else:
                return mid
                
        return -1
            
