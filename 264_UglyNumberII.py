from heapq import *
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        i2, i3, i5 = 0, 0, 0
        all_nums = [1] * n
        for i in range(1, n):
            curr_num = min(2*all_nums[i2], 3*all_nums[i3], 5*all_nums[i5])
            all_nums[i] = curr_num

            if curr_num == 2*all_nums[i2]:
                i2 += 1
            if curr_num == 3*all_nums[i3]:
                i3 += 1
            if curr_num == 5*all_nums[i5]:
                i5 += 1

        return all_nums[-1]

